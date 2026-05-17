(function () {
  const STORAGE_KEY = 'artistBeautyPersistentPlayer';
  const player = document.getElementById('persistent-player');
  const audio = document.getElementById('persistent-audio');
  const playBtn = document.getElementById('persist-play');
  const songText = document.getElementById('persist-song');
  const artistText = document.getElementById('persist-artist');
  const pageData = window.PAGE_PLAYER_DATA || {};
  const hasPagePlayer = !!document.getElementById('audio-player-bar');

  if (!audio || !player || !playBtn || !songText || !artistText) return;

  const stored = loadStoredState();
  const hasStoredSong = stored && stored.songUrl;
  const sameSong = hasStoredSong && pageData.songUrl && stored.songUrl === pageData.songUrl;

  audio.volume = 0.5;
  audio.loop = true;
  audio.autoplay = true;

  if (hasStoredSong) {
    audio.src = stored.songUrl;
    if (stored.currentTime) audio.currentTime = stored.currentTime;
    songText.textContent = stored.songTitle || pageData.songTitle || 'Canción en reproducción';
    artistText.textContent = stored.artistName
      ? `${stored.artistName} · ${stored.brandName || ''}`
      : (pageData.artistName ? `${pageData.artistName} · ${pageData.brandName || ''}` : '—');
  }

  if (pageData.songUrl && (!audio.src || audio.src !== pageData.songUrl)) {
    audio.src = pageData.songUrl;
    audio.currentTime = 0;
    songText.textContent = pageData.songTitle || songText.textContent;
    artistText.textContent = pageData.artistName
      ? `${pageData.artistName} · ${pageData.brandName || ''}`
      : artistText.textContent;
    showPlayer();
    audio.play().catch(() => {});
  }

  function showPlayer() {
    player.classList.add('visible');
  }

  function hidePlayer() {
    player.classList.remove('visible');
  }

  function updateButton() {
    playBtn.textContent = audio.paused ? '▶' : '⏸';
  }

  function saveState() {
    if (!audio.src) return;
    const state = {
      songUrl: audio.src,
      songTitle: songText.textContent,
      artistName: pageData.artistName || (stored && stored.artistName) || '',
      brandName: pageData.brandName || (stored && stored.brandName) || '',
      currentTime: audio.currentTime,
      playing: !audio.paused && !audio.ended,
      updated: Date.now(),
    };
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (error) {
      // localStorage puede estar deshabilitado.
    }
  }

  function loadStoredState() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (error) {
      return null;
    }
  }

  function throttle(fn, delay) {
    let timeout = null;
    return function () {
      if (timeout) return;
      timeout = setTimeout(() => {
        fn();
        timeout = null;
      }, delay);
    };
  }

  audio.addEventListener('loadedmetadata', () => {
    if (sameSong && stored && stored.currentTime && audio.duration) {
      audio.currentTime = Math.min(stored.currentTime, audio.duration);
    }
  });

  audio.addEventListener('play', () => {
    updateButton();
    if (!hasPagePlayer) showPlayer();
    saveState();
  });

  audio.addEventListener('pause', () => {
    updateButton();
    saveState();
  });

  audio.addEventListener('ended', () => {
    updateButton();
    saveState();
  });

  audio.addEventListener('timeupdate', throttle(saveState, 1000));

  playBtn.addEventListener('click', () => {
    if (!audio.src && pageData.songUrl) {
      audio.src = pageData.songUrl;
    }
    if (audio.paused) {
      audio.play().catch(() => {});
    } else {
      audio.pause();
    }
  });

  if (sameSong && stored.playing && !hasPagePlayer) {
    showPlayer();
    audio.play().catch(() => {});
  }

  if (hasStoredSong && !hasPagePlayer && sameSong) {
    showPlayer();
  }

  window.addEventListener('beforeunload', saveState);
})();
