// Show or hide the Latin column; remembered per reader where storage allows.
(function () {
  var head = document.querySelector('.ch-head');
  if (!head) return;
  var key = 'wyclif-latin', hidden = false;
  try { hidden = localStorage.getItem(key) === 'hidden'; } catch (e) {}
  var b = document.createElement('button');
  b.type = 'button'; b.className = 'latin-toggle';
  function set(h) {
    document.body.classList.toggle('no-latin', h);
    b.textContent = h ? 'Show the Latin' : 'Hide the Latin';
    b.setAttribute('aria-pressed', h ? 'true' : 'false');
    try { localStorage.setItem(key, h ? 'hidden' : 'shown'); } catch (e) {}
  }
  b.addEventListener('click', function () { set(!document.body.classList.contains('no-latin')); });
  head.appendChild(b); set(hidden);
})();
