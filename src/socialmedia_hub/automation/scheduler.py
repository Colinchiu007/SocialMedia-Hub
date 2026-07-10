"""Task scheduler for social media automation."""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable

logger = logging.getLogger("socialmedia_hub.automation.scheduler")


class TaskStatus(str, Enum):
    """Task status enum."""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    """Scheduled task."""
    id: str
    name: str
    func: Callable
    args: tuple = ()
    kwargs: dict[str, Any] = field(default_factory=dict)
    interval: float = 3600  # Default: 1 hour
    max_retries: int = 3
    status: TaskStatus = TaskStatus.PENDING
    last_run: float = 0
    next_run: float = 0
    run_count: int = 0
    error_count: int = 0


class TaskScheduler:
    """Schedule and run periodic tasks.

    Features:
    - Add/remove tasks
    - Configurable intervals
    - Automatic retry on failure
    - Task status tracking
    """

    def __init__(self) -> None:
        """Initialize the scheduler."""
        self._tasks: dict[str, Task] = {}
        self._running = False
        self._task_id_counter = 0

    def add_task(
        self,
        name: str,
        func: Callable,
        interval: float = 3600,
        args: tuple = (),
        kwargs: dict[str, Any] | None = None,
        max_retries: int = 3,
        run_immediately: bool = False,
    ) -> str:
        """Add a task to the scheduler.

        Args:
            name: Task name
            func: Function to call
            interval: Interval in seconds between runs
            args: Positional arguments for the function
            kwargs: Keyword arguments for the function
            max_retries: Maximum retries on failure
            run_immediately: Whether to run immediately

        Returns:
            Task ID
        """
        self._task_id_counter += 1
        task_id = f"task_{self._task_id_counter}"

        task = Task(
            id=task_id,
            name=name,
            func=func,
            args=args,
            kwargs=kwargs or {},
            interval=interval,
            max_retries=max_retries,
            next_run=time.time() if run_immediately else time.time() + interval,
        )

        self._tasks[task_id] = task
        logger.info(f"Added task: {name} (ID: {task_id}, interval: {interval}s)")
        return task_id

    def remove_task(self, task_id: str) -> bool:
        """Remove a task from the scheduler.

        Args:
            task_id: Task ID to remove

        Returns:
            True if task was removed
        """
        if task_id in self._tasks:
            task = self._tasks.pop(task_id)
            logger.info(f"Removed task: {task.name}")
            return True
        return False

    def get_task(self, task_id: str) -> Task | None:
        """Get task by ID."""
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks."""
        return list(self._tasks.values())

    async def run_task(self, task: Task) -> dict[str, Any]:
        """Run a single task.

        Args:
            task: Task to run

        Returns:
            Task result or error
        """
        task.status = TaskStatus.RUNNING
        task.last_run = time.time()

        for attempt in range(task.max_retries):
            try:
                if asyncio.iscoroutinefunction(task.func):
                    result = await task.func(*task.args, **task.kwargs)
                else:
                    result = task.func(*task.args, **task.kwargs)

                task.status = TaskStatus.COMPLETED
                task.run_count += 1
                task.next_run = time.time() + task.interval

                logger.info(f"Task completed: {task.name} (run #{task.run_count})")
                return {"status": "success", "result": result}

            except Exception as e:
                task.error_count += 1
                if attempt == task.max_retries - 1:
                    task.status = TaskStatus.FAILED
                    task.next_run = time.time() + task.interval
                    logger.error(f"Task failed: {task.name} - {e}")
                    return {"status": "error", "error": str(e)}

        task.status = TaskStatus.PENDING
        task.next_run = time.time() + task.interval
        return {"status": "retry", "next_run": task.next_run}

    async def run_pending_tasks(self) -> list[dict[str, Any]]:
        """Run all pending tasks.

        Returns:
            List of task results
        """
        results = []
        now = time.time()

        for task in self._tasks.values():
            if task.status == TaskStatus.PENDING and task.next_run <= now:
                result = await self.run_task(task)
                results.append({"task_id": task.id, "name": task.name, **result})

        return results

    async def start(self, check_interval: float = 1.0) -> None:
        """Start the scheduler loop.

        Args:
            check_interval: How often to check for pending tasks (seconds)
        """
        self._running = True
        logger.info("Scheduler started")

        while self._running:
            await self.run_pending_tasks()
            await asyncio.sleep(check_interval)

    def stop(self) -> None:
        """Stop the scheduler loop."""
        self._running = False
        logger.info("Scheduler stopped")

    def get_stats(self) -> dict[str, Any]:
        """Get scheduler statistics."""
        tasks = list(self._tasks.values())
        return {
            "total_tasks": len(tasks),
            "pending": sum(1 for t in tasks if t.status == TaskStatus.PENDING),
            "running": sum(1 for t in tasks if t.status == TaskStatus.RUNNING),
            "completed": sum(1 for t in tasks if t.status == TaskStatus.COMPLETED),
            "failed": sum(1 for t in tasks if t.status == TaskStatus.FAILED),
            "total_runs": sum(t.run_count for t in tasks),
            "total_errors": sum(t.error_count for t in tasks),
        }
