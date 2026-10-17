/* thư viện 86 style: lọc theo nhóm, tìm kiếm, nút Chép chỉ chép "style <slug>" */
(() => {
  const S = (window.STYLES || []).slice().sort((a, b) => (a.from !== 'MotionFly') - (b.from !== 'MotionFly'));
  const gal = document.getElementById('gal'), q = document.getElementById('q'), cnt = document.getElementById('cnt'), more = document.getElementById('more');
  const GH = 'https://github.com/andyluu98/VideoMotion/blob/master/styles/';
  const esc = t => String(t || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const groups = ['Tất cả', ...new Set(S.map(s => s.group))];
  let g = 'Tất cả', all = false;
  document.getElementById('fb').outerHTML = groups.map(x => `<button type="button" data-g="${x}" class="${x === g ? 'on' : ''}">${x}</button>`).join('');
  const tile = (st, i) => {
    const tags = (st.mood || '').split(',').map(t => t.trim()).filter(Boolean).slice(0, 4);
    return `<article class="st" data-i="${i}">
    <a class="th" href="${GH}${st.slug}.md" target="_blank" rel="noopener">${st.img ? `<img src="${st.img}" alt="Minh họa style ${esc(st.name)}" loading="lazy" width="800" height="450">` : ''}<span class="src">${st.from === 'MotionFly' ? 'khung video' : 'khung slide'}</span></a>
    <div class="b"><div class="n">${esc(st.name)}</div><div class="s">style ${st.slug}</div>
      <div class="md">${esc(st.use)}</div>
      <div class="tg">${tags.map(t => `<span>${esc(t)}</span>`).join('')}</div>
      <div class="f">${esc(st.fonts)}</div>
      <div class="act"><button type="button" class="p" data-a="copy">Chép</button><a href="${GH}${st.slug}.md" target="_blank" rel="noopener" title="Đọc thẻ style trên GitHub">Thẻ ↗</a></div></div></article>`;
  };
  const draw = () => {
    const k = q.value.trim().toLowerCase();
    const list = S.map((s, i) => [s, i]).filter(([s]) => (g === 'Tất cả' || s.group === g) && (!k || (s.name + s.slug + s.mood + s.use + s.fonts).toLowerCase().includes(k)));
    const show = all || k || g !== 'Tất cả' ? list : list.slice(0, 16);
    cnt.textContent = list.length + ' style';
    gal.innerHTML = show.map(([s, i]) => tile(s, i)).join('');
    more.style.display = show.length < list.length ? '' : 'none';
    window.reveal && window.reveal(gal.querySelectorAll('.st'));
  };
  gal.addEventListener('click', async e => {
    const b = e.target.closest('button[data-a]'); if (!b) return;
    const st = S[+b.closest('.st').dataset.i];
    const ok = await window.copyText(`style ${st.slug}`);
    window.say(ok ? `Đã chép "style ${st.slug}". Dán vào cuối yêu cầu làm video.` : 'Trình duyệt chặn chép, hãy gõ tay: style ' + st.slug);
    if (ok) { b.textContent = 'Đã chép'; setTimeout(() => b.textContent = 'Chép', 1400); }
  });
  document.querySelector('.filters').addEventListener('click', e => {
    const b = e.target.closest('button[data-g]'); if (!b) return;
    g = b.dataset.g; document.querySelectorAll('.filters button').forEach(x => x.classList.toggle('on', x === b)); draw();
  });
  more.querySelector('button').addEventListener('click', () => { all = true; draw(); });
  q.addEventListener('input', draw);
  draw();
})();
