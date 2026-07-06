// SocialMedia-Hub Chrome Extension - Background Service Worker

const API_BASE = 'http://localhost:8000';

// Listen for extension icon click
chrome.action.onClicked.addListener((tab) => {
  chrome.sidePanel.open({ windowId: tab.windowId });
});

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'analyze') {
    analyzePage(request.data)
      .then(sendResponse)
      .catch((error) => sendResponse({ error: error.message }));
    return true; // Keep message channel open for async response
  }
  
  if (request.action === 'fetchVideo') {
    fetchVideoData(request.videoId, request.platform)
      .then(sendResponse)
      .catch((error) => sendResponse({ error: error.message }));
    return true;
  }
  
  if (request.action === 'fetchUser') {
    fetchUserData(request.userId, request.platform)
      .then(sendResponse)
      .catch((error) => sendResponse({ error: error.message }));
    return true;
  }
});

// Analyze current page
async function analyzePage(data) {
  const platform = detectPlatform(data.url);
  
  if (!platform) {
    return { error: 'Unsupported platform' };
  }
  
  try {
    const result = await callAPI(`/api/v1/${platform}/analyze`, {
      url: data.url,
      ...data
    });
    return result;
  } catch (error) {
    return { error: error.message };
  }
}

// Fetch video data
async function fetchVideoData(videoId, platform) {
  try {
    const result = await callAPI(`/api/v1/${platform}/fetch_video`, {
      video_id: videoId
    });
    return result;
  } catch (error) {
    return { error: error.message };
  }
}

// Fetch user data
async function fetchUserData(userId, platform) {
  try {
    const result = await callAPI(`/api/v1/${platform}/fetch_user`, {
      user_id: userId
    });
    return result;
  } catch (error) {
    return { error: error.message };
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

// Call API endpoint
async function callAPI(endpoint, params = {}) {
  const apiKey = await getApiKey();
  
  if (!apiKey) {
    throw new Error('API key not configured');
  }
  
  const url = new URL(`${API_BASE}${endpoint}`);
  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== null) {
      url.searchParams.append(key, value);
    }
  });
  
  const response = await fetch(url.toString(), {
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json'
    }
  });
  
  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }
  
  return response.json();
}

// Get API key from storage
async function getApiKey() {
  const result = await chrome.storage.local.get(['apiKey']);
  return result.apiKey || null;
}

// Set API key in storage
async function setApiKey(apiKey) {
  await chrome.storage.local.set({ apiKey });
}

// Open side panel
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'openSidePanel') {
    chrome.sidePanel.open({ windowId: sender.tab.windowId });
    sendResponse({ success: true });
  }
});
