/* landing VideoMotion: hiện dần khi cuộn, tiêu đề, video có tiếng, tab, chép lệnh */
(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  gsap.registerPlugin(SplitText, ScrambleTextPlugin);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* tiện ích dùng chung với gallery.js */
  const toast = document.createElement('div'); toast.className = 'toast'; document.body.append(toast);
  window.say = t => { toast.textContent = t; toast.classList.add('on'); clearTimeout(toast._t); toast._t = setTimeout(() => toast.classList.remove('on'), 2600); };
  window.copyText = async t => {
    try { await navigator.clipboard.writeText(t); return true; }
    catch (_) { const a = document.createElement('textarea'); a.value = t; document.body.append(a); a.select(); const ok = document.execCommand('copy'); a.remove(); return ok; }
  };
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    io.unobserve(e.target);
    gsap.to(e.target, { opacity: 1, y: 0, duration: .8, ease: 'power3.out', delay: (+e.target.dataset.d || 0) * .08 });
  }), { rootMargin: '0px 0px -8% 0px' });
  window.reveal = nodes => [...nodes].forEach((n, i) => { if (reduce) return; n.classList.add('rv'); n.dataset.d = i % 4; io.observe(n); });
  window.reveal($$('section h2, section .sub, .strip figure, .tw, .step, .inst .i, .how div'));

  /* tiêu đề hero bay vào từng ký tự, nhãn giải mã */
  if (!reduce) {
    const h = new SplitText('h1', { type: 'words,chars' });
    gsap.from(h.chars, { yPercent: 110, opacity: 0, rotate: 8, duration: .9, ease: 'expo.out', stagger: .03 });
    gsap.from('.hero .kick', { duration: 1, scrambleText: { text: ' ', chars: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', speed: .6 } });
    gsap.from('.lead, .cta, .checks', { y: 20, opacity: 0, duration: .8, ease: 'power3.out', stagger: .1, delay: .3 });
    gsap.from('.phone', { y: 60, opacity: 0, rotate: 4, duration: 1.2, ease: 'expo.out', delay: .2 });
  }

  /* video mẫu: tự chạy không tiếng, bấm để nghe */
  const v = $('.phone video'), snd = $('.phone .snd');
  snd.onclick = () => { v.muted = !v.muted; if (!v.muted) { v.currentTime = 0; v.play(); } snd.textContent = v.muted ? 'Bật tiếng' : 'Tắt tiếng'; };

  /* tab hệ điều hành, nút chép lệnh cài đặt */
  const inst = $('#cai-dat');
  inst.dataset.os = /Win/.test(navigator.platform) ? 'win' : 'mac';
  $$('.os button').forEach(b => { b.classList.toggle('on', b.dataset.os === inst.dataset.os); b.onclick = () => { inst.dataset.os = b.dataset.os; $$('.os button').forEach(x => x.classList.toggle('on', x === b)); }; });
  $$('.cmd').forEach(c => { const b = document.createElement('button'); b.className = 'cp'; b.textContent = 'Sao chép'; c.append(b); b.onclick = async () => { const ok = await window.copyText(c.firstChild.textContent.trim()); b.textContent = ok ? 'Đã chép' : 'Lỗi'; setTimeout(() => b.textContent = 'Sao chép', 1500); }; });
})();
