// SocialMedia-Hub Content Script
// Runs on supported social media pages

(function() {
  'use strict';

  // Listen for messages from background/sidepanel
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'analyze') {
      analyzePage()
        .then(sendResponse)
        .catch(error => sendResponse({ error: error.message }));
      return true;
    }

    if (request.action === 'getPageData') {
      sendResponse(getPageData());
      return true;
    }
  });

  // Analyze current page
  async function analyzePage() {
    const pageData = getPageData();
    return pageData;
  }

  // Get page data
  function getPageData() {
    const url = window.location.href;
    const platform = detectPlatform(url);
    
    const data = {
      url,
      platform,
      title: document.title,
      timestamp: new Date().toISOString()
    };

    // Extract platform-specific data
    switch (platform) {
      case 'tiktok':
      case 'douyin':
        Object.assign(data, extractTikTokData());
        break;
      case 'instagram':
        Object.assign(data, extractInstagramData());
        break;
      case 'youtube':
        Object.assign(data, extractYouTubeData());
        break;
      case 'twitter':
      case 'x':
        Object.assign(data, extractTwitterData());
        break;
      case 'bilibili':
        Object.assign(data, extractBilibiliData());
        break;
    }

    return data;
  }

  // Detect platform
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

  // Extract TikTok/Douyin data
  function extractTikTokData() {
    const data = {};
    
    // Try to extract video data from page
    const videoElement = document.querySelector('video');
    if (videoElement) {
      data.hasVideo = true;
      data.videoSrc = videoElement.src;
    }

    // Extract user info
    const userLink = document.querySelector('[data-e2e="user-avatar"] a, .user-info a');
    if (userLink) {
      data.author = userLink.textContent?.trim();
      data.authorUrl = userLink.href;
    }

    // Extract stats
    const statsElements = document.querySelectorAll('[data-e2e*="count"], .like-count, .comment-count');
    data.stats = {};
    statsElements.forEach(el => {
      const text = el.textContent?.trim();
      const label = el.getAttribute('data-e2e') || el.className;
      if (text) {
        data.stats[label] = text;
      }
    });

    return data;
  }

  // Extract Instagram data
  function extractInstagramData() {
    const data = {};
    
    // Extract username
    const usernameEl = document.querySelector('header section h2, .Username');
    if (usernameEl) {
      data.author = usernameEl.textContent?.trim();
    }

    // Extract bio
    const bioEl = document.querySelector('header section div[class*="bio"], .bio');
    if (bioEl) {
      data.bio = bioEl.textContent?.trim();
    }

    // Extract stats
    const statsEl = document.querySelectorAll('header section ul li');
    data.stats = {};
    statsEl.forEach((el, index) => {
      const text = el.textContent?.trim();
      if (text) {
        const labels = ['posts', 'followers', 'following'];
        data.stats[labels[index] || `stat_${index}`] = text;
      }
    });

    return data;
  }

  // Extract YouTube data
  function extractYouTubeData() {
    const data = {};
    
    // Extract video title
    const titleEl = document.querySelector('h1.ytd-watch-metadata, h1.title');
    if (titleEl) {
      data.title = titleEl.textContent?.trim();
    }

    // Extract channel name
    const channelEl = document.querySelector('#channel-name a, ytd-channel-name a');
    if (channelEl) {
      data.author = channelEl.textContent?.trim();
    }

    // Extract view count
    const viewEl = document.querySelector('#info-text span.view-count, .view-count');
    if (viewEl) {
      data.views = viewEl.textContent?.trim();
    }

    return data;
  }

  // Extract Twitter data
  function extractTwitterData() {
    const data = {};
    
    // Extract tweet text
    const tweetEl = document.querySelector('[data-testid="tweetText"], .tweet-text');
    if (tweetEl) {
      data.content = tweetEl.textContent?.trim();
    }

    // Extract username
    const usernameEl = document.querySelector('[data-testid="User-Name"], .username');
    if (usernameEl) {
      data.author = usernameEl.textContent?.trim();
    }

    return data;
  }

  // Extract Bilibili data
  function extractBilibiliData() {
    const data = {};
    
    // Extract video title
    const titleEl = document.querySelector('h1.video-title, .video-title');
    if (titleEl) {
      data.title = titleEl.textContent?.trim();
    }

    // Extract author
    const authorEl = document.querySelector('.author-name, .user-name');
    if (authorEl) {
      data.author = authorEl.textContent?.trim();
    }

    // Extract stats
    const viewEl = document.querySelector('.view-count, .play-count');
    if (viewEl) {
      data.views = viewEl.textContent?.trim();
    }

    return data;
  }
})();
