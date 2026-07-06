// SocialMedia-Hub Sidepanel JavaScript

const API_BASE = 'http://localhost:8000';

// DOM Elements
const apiKeyInput = document.getElementById('apiKeyInput');
const saveApiKeyBtn = document.getElementById('saveApiKeyBtn');
const apiKeyStatus = document.getElementById('apiKeyStatus');
const pageAnalysis = document.getElementById('pageAnalysis');
const pageInfo = document.getElementById('pageInfo');
const pageUrl = document.getElementById('pageUrl');
const pagePlatform = document.getElementById('pagePlatform');
const analyzeBtn = document.getElementById('analyzeBtn');
const analysisResults = document.getElementById('analysisResults');
const resultsContent = document.getElementById('resultsContent');
const quickActions = document.getElementById('quickActions');
const history = document.getElementById('history');
const historyList = document.getElementById('historyList');
const loading = document.getElementById('loading');

// Initialize
document.addEventListener('DOMContentLoaded', init);

async function init() {
  await loadApiKey();
  await loadHistory();
  setupEventListeners();
  detectCurrentPage();
}

// Load API key from storage
async function loadApiKey() {
  const result = await chrome.storage.local.get(['apiKey']);
  if (result.apiKey) {
    apiKeyInput.value = result.apiKey;
    apiKeyStatus.textContent = 'API key configured';
    apiKeyStatus.className = 'status success';
    pageAnalysis.classList.remove('hidden');
  }
}

// Save API key
async function saveApiKey() {
  const apiKey = apiKeyInput.value.trim();
  if (!apiKey) {
    apiKeyStatus.textContent = 'Please enter an API key';
    apiKeyStatus.className = 'status error';
    return;
  }

  await chrome.storage.local.set({ apiKey });
  apiKeyStatus.textContent = 'API key saved!';
  apiKeyStatus.className = 'status success';
  pageAnalysis.classList.remove('hidden');
}

// Load history from storage
async function loadHistory() {
  const result = await chrome.storage.local.get(['analysisHistory']);
  const historyData = result.analysisHistory || [];
  
  if (historyData.length === 0) {
    historyList.innerHTML = '<p>No recent analyses</p>';
    return;
  }

  historyList.innerHTML = historyData.slice(0, 5).map(item => `
    <div class="history-item" data-url="${item.url}">
      <h4>${item.title || 'Untitled'}</h4>
      <p>${item.platform} • ${item.timestamp}</p>
    </div>
  `).join('');
}

// Detect current page
async function detectCurrentPage() {
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab && tab.url) {
      const platform = detectPlatform(tab.url);
      pageUrl.textContent = tab.url;
      pagePlatform.textContent = `Platform: ${platform || 'Unknown'}`;
      
      if (platform) {
        analyzeBtn.disabled = false;
      } else {
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Unsupported Platform';
      }
    }
  } catch (error) {
    console.error('Error detecting page:', error);
  }
}

// Detect platform from URL
function detectPlatform(url) {
  if (url.includes('tiktok.com')) return 'tiktok';
  if (url.includes('douyin.com')) return 'douyin';
  if (url.includes('instagram.com')) return 'instagram';
  if (url.includes('youtube.com') || url.includes('youtu.be')) return 'youtube';
  if (url.includes('twitter.com') || url.includes('x.com')) return 'twitter';
  if (url.includes('bilibili.com')) return 'bilibili';
  if (url.includes('xiaohongshu.com')) return 'xiaohongshu';
  return null;
}

// Analyze current page
async function analyzeCurrentPage() {
  showLoading(true);
  
  try {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const platform = detectPlatform(tab.url);
    
    if (!platform) {
      throw new Error('Unsupported platform');
    }

    // Send message to content script
    const response = await chrome.tabs.sendMessage(tab.id, {
      action: 'analyze',
      data: { url: tab.url, platform }
    });

    if (response.error) {
      throw new Error(response.error);
    }

    displayResults(response);
    saveToHistory(tab.url, tab.title, platform);
    
  } catch (error) {
    showError(error.message);
  } finally {
    showLoading(false);
  }
}

// Display results
function displayResults(data) {
  analysisResults.classList.remove('hidden');
  
  if (data.error) {
    resultsContent.innerHTML = `<div class="result-item"><h4>Error</h4><p>${data.error}</p></div>`;
    return;
  }

  const results = data.data || data;
  let html = '';

  if (results.title) {
    html += `<div class="result-item"><h4>Title</h4><p>${results.title}</p></div>`;
  }
  if (results.author) {
    html += `<div class="result-item"><h4>Author</h4><p>${results.author}</p></div>`;
  }
  if (results.stats) {
    html += `<div class="result-item"><h4>Statistics</h4>`;
    for (const [key, value] of Object.entries(results.stats)) {
      html += `<p>${key}: ${value}</p>`;
    }
    html += `</div>`;
  }

  resultsContent.innerHTML = html || '<p>No data available</p>';
}

// Show error
function showError(message) {
  resultsContent.innerHTML = `<div class="result-item"><h4>Error</h4><p>${message}</p></div>`;
  analysisResults.classList.remove('hidden');
}

// Show/hide loading
function showLoading(show) {
  loading.classList.toggle('hidden', !show);
  analyzeBtn.disabled = show;
}

// Save to history
async function saveToHistory(url, title, platform) {
  const result = await chrome.storage.local.get(['analysisHistory']);
  const historyData = result.analysisHistory || [];
  
  historyData.unshift({
    url,
    title,
    platform,
    timestamp: new Date().toLocaleString()
  });

  // Keep only last 10 items
  await chrome.storage.local.set({ analysisHistory: historyData.slice(0, 10) });
  await loadHistory();
}

// Setup event listeners
function setupEventListeners() {
  saveApiKeyBtn.addEventListener('click', saveApiKey);
  analyzeBtn.addEventListener('click', analyzeCurrentPage);

  // Quick action buttons
  document.querySelectorAll('.action-btn').forEach(btn => {
    btn.addEventListener('click', () => handleQuickAction(btn.dataset.action));
  });

  // History item clicks
  historyList.addEventListener('click', (e) => {
    const item = e.target.closest('.history-item');
    if (item) {
      const url = item.dataset.url;
      if (url) {
        chrome.tabs.create({ url });
      }
    }
  });
}

// Handle quick actions
async function handleQuickAction(action) {
  showLoading(true);
  
  try {
    const apiKey = await chrome.storage.local.get(['apiKey']);
    if (!apiKey.apiKey) {
      throw new Error('Please configure API key first');
    }

    const response = await fetch(`${API_BASE}/api/v1/health/check`, {
      headers: { 'Authorization': `Bearer ${apiKey.apiKey}` }
    });

    if (!response.ok) {
      throw new Error('API connection failed');
    }

    // For now, show a message
    displayResults({ message: `${action} feature coming soon!` });
    
  } catch (error) {
    showError(error.message);
  } finally {
    showLoading(false);
  }
}
