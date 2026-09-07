/* Tiansight 侍天 — profile pages: preview which auxiliary titles show, at most three.
   The build reads the "show" flags in people/profiles.json; this only previews combinations
   on screen so the flags can be decided before editing the data. Nothing is persisted. */
(function () {
  var bar = document.querySelector('.switchbar');
  if (!bar) return;
  var boxes = Array.prototype.slice.call(bar.querySelectorAll('input[type="checkbox"]'));
  var slots = Array.prototype.slice.call(document.querySelectorAll('[data-aux-slot]'));
  var warn = bar.querySelector('.over');
  var MAX = 3;

  function apply() {
    var on = boxes.filter(function (b) { return b.checked; });
    var over = on.length > MAX;
    warn.hidden = !over;
    boxes.forEach(function (b) { b.disabled = !b.checked && on.length >= MAX; });
    var labels = on.slice(0, MAX).map(function (b) { return b.value; });
    slots.forEach(function (slot) {
      slot.textContent = '';
      labels.forEach(function (text) {
        var span = document.createElement('span');
        span.textContent = text;
        slot.appendChild(span);
      });
    });
  }
  boxes.forEach(function (b) { b.addEventListener('change', apply); });
  apply();
})();
