"""Whisper-based speech-to-text transcription for video content."""

from __future__ import annotations

import logging
import tempfile
from pathlib import Path
from typing import Any

logger = logging.getLogger("socialmedia_hub.transcription.whisper")


class WhisperTranscriber:
    """Transcribe video audio to text using Whisper.

    This class uses faster-whisper for efficient speech-to-text transcription.
    """

    def __init__(self, model_size: str = "base", device: str = "cpu") -> None:
        """Initialize the transcriber.

        Args:
            model_size: Whisper model size (tiny, base, small, medium, large)
            device: Device to use (cpu, cuda, auto)
        """
        self.model_size = model_size
        self.device = device
        self._model = None

    def _get_model(self):
        """Lazy load the Whisper model."""
        if self._model is None:
            try:
                from faster_whisper import WhisperModel
                logger.info(f"Loading Whisper model: {self.model_size}")
                self._model = WhisperModel(self.model_size, device=self.device)
                logger.info("Whisper model loaded successfully")
            except ImportError:
                raise ImportError(
                    "faster-whisper is required. Install with: pip install faster-whisper"
                )
        return self._model

    def transcribe_file(
        self,
        audio_path: str | Path,
        language: str | None = None,
        task: str = "transcribe",
    ) -> dict[str, Any]:
        """Transcribe an audio file.

        Args:
            audio_path: Path to audio file
            language: Language code (e.g., 'en', 'zh') or None for auto-detect
            task: Task type ('transcribe' or 'translate')

        Returns:
            Transcription result dictionary
        """
        model = self._get_model()
        audio_path = str(audio_path)

        try:
            segments, info = model.transcribe(
                audio_path,
                language=language,
                task=task,
                beam_size=5,
                vad_filter=True,
            )

            # Collect all segments
            full_text = []
            segments_list = []
            for segment in segments:
                full_text.append(segment.text)
                segments_list.append({
                    "start": segment.start,
                    "end": segment.end,
                    "text": segment.text,
                })

            return {
                "text": " ".join(full_text).strip(),
                "segments": segments_list,
                "language": info.language,
                "language_probability": info.language_probability,
                "duration": info.duration,
            }

        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            return {"text": "", "segments": [], "error": str(e)}

    def transcribe_video(
        self,
        video_path: str | Path,
        language: str | None = None,
        extract_audio: bool = True,
    ) -> dict[str, Any]:
        """Transcribe video by first extracting audio.

        Args:
            video_path: Path to video file
            language: Language code or None for auto-detect
            extract_audio: Whether to extract audio first

        Returns:
            Transcription result dictionary
        """
        video_path = Path(video_path)

        if not video_path.exists():
            return {"text": "", "segments": [], "error": f"File not found: {video_path}"}

        if extract_audio:
            # Extract audio to temporary file
            audio_path = self._extract_audio(video_path)
            if audio_path is None:
                return {"text": "", "segments": [], "error": "Failed to extract audio"}
        else:
            audio_path = video_path

        try:
            result = self.transcribe_file(audio_path, language)
            return result
        finally:
            # Clean up temporary audio file
            if extract_audio and audio_path != video_path:
                try:
                    Path(audio_path).unlink()
                except Exception:
                    pass

    def _extract_audio(self, video_path: Path) -> str | None:
        """Extract audio from video file.

        Args:
            video_path: Path to video file

        Returns:
            Path to extracted audio file, or None on failure
        """
        try:
            import subprocess

            # Create temporary file for audio
            temp_dir = tempfile.mkdtemp()
            audio_path = Path(temp_dir) / f"{video_path.stem}.wav"

            # Use ffmpeg to extract audio
            cmd = [
                "ffmpeg",
                "-i", str(video_path),
                "-vn",  # No video
                "-acodec", "pcm_s16le",  # PCM 16-bit
                "-ar", "16000",  # 16kHz sample rate
                "-ac", "1",  # Mono
                str(audio_path),
                "-y",  # Overwrite
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                timeout=60,
            )

            if result.returncode == 0 and audio_path.exists():
                return str(audio_path)
            else:
                logger.error(f"FFmpeg error: {result.stderr.decode()}")
                return None

        except Exception as e:
            logger.error(f"Audio extraction failed: {e}")
            return None

    def transcribe_url(
        self,
        url: str,
        language: str | None = None,
    ) -> dict[str, Any]:
        """Download video from URL and transcribe.

        Args:
            url: Video URL
            language: Language code or None for auto-detect

        Returns:
            Transcription result dictionary
        """
        try:
            import yt_dlp

            # Download video to temporary file
            with tempfile.TemporaryDirectory() as temp_dir:
                output_path = Path(temp_dir) / "video.%(ext)s"

                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": str(output_path),
                    "quiet": True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)

                # Transcribe the downloaded file
                result = self.transcribe_file(filename, language)
                result["title"] = info.get("title")
                result["url"] = url
                return result

        except Exception as e:
            logger.error(f"URL transcription failed: {e}")
            return {"text": "", "segments": [], "error": str(e)}


# Global transcriber instance
whisper_transcriber = WhisperTranscriber()
