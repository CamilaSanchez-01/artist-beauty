/* =============================================================
   Reproductor de canción icónica del/la artista.
   Esta es la mejora estrella del proyecto vs la actividad 3.2.

   Cuando se renderiza la sección de top 5 best sellers,
   la canción icónica del artista se reproduce automáticamente
   (con respeto a la política de autoplay del navegador).
   ============================================================= */
(function () {
  const playerBar = document.getElementById('audio-player-bar');
  const audio    = document.getElementById('iconic-song') || document.getElementById('persistent-audio');
  const playBtn  = document.getElementById('play-btn');
  const status   = document.getElementById('player-status');
  const grid     = document.getElementById('bestseller-grid');

  if (!playerBar || !audio || !playBtn) return;

  const pageSongUrl = playerBar.dataset.songUrl;
  if (pageSongUrl && (!audio.src || audio.src !== pageSongUrl)) {
    audio.src = pageSongUrl;
  }

  function setPlaying(playing) {
    if (playing) {
      playerBar.classList.add('playing');
      playBtn.textContent = '⏸ Pausar';
      status.textContent = '♪ Sonando…';
    } else {
      playerBar.classList.remove('playing');
      playBtn.textContent = '▶ Reproducir';
      status.textContent = 'Pausado';
    }
  }

  audio.volume = 0.5;
  audio.loop = true;
  audio.autoplay = true;

  audio.addEventListener('play',  () => setPlaying(true));
  audio.addEventListener('pause', () => setPlaying(false));
  audio.addEventListener('ended', () => setPlaying(false));
  audio.addEventListener('error', () => {
    status.textContent = '⚠ No se pudo cargar el audio (revisa la URL).';
  });

  playBtn.addEventListener('click', () => {
    if (audio.paused) audio.play().catch(handleAutoplayBlocked);
    else audio.pause();
  });

  function handleAutoplayBlocked() {
    status.textContent = '⚠ Da clic en Reproducir (autoplay bloqueado).';
  }

  /* ---------- AUTOPLAY al ver los best sellers ----------
     IntersectionObserver dispara el play cuando la sección
     de best sellers entra en pantalla. Si el navegador bloquea
     el autoplay (Chrome/Safari), se queda esperando el clic. */
  if (grid && 'IntersectionObserver' in window) {
    let triggered = false;
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && !triggered) {
          triggered = true;
          status.textContent = 'Intentando autoplay…';
          audio.play().catch(handleAutoplayBlocked);
        }
      });
    }, { threshold: 0.25 });
    observer.observe(grid);
  }

  /* ---------- Hover en una tarjeta best seller ----------
     Si el usuario pasa el mouse sobre cualquier best seller,
     intentamos asegurar que la canción esté sonando. */
  if (grid) {
    grid.querySelectorAll('.bestseller').forEach((card) => {
      card.addEventListener('mouseenter', () => {
        if (audio.paused) audio.play().catch(handleAutoplayBlocked);
      });
    });
  }
})();
