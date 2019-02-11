;(function () {
  'use strict';

  const btnScrollDown = document.querySelectorAll('.scroll_down');
  for (let i of btnScrollDown) {
      i.onclick = function scroll() {
          if (window.pageYOffset < (i.dataset.px*1 - i.dataset.stopper*1)) {
            window.scrollBy(0, i.dataset.speed*1);
            setTimeout(scroll, 0);
          } else if (window.pageYOffset < i.dataset.px*1) {
            window.scrollBy(0, 1);
            setTimeout(scroll, 0);
          }
          if (window.pageYOffset > i.dataset.px*1) {
            window.scrollTo(0, i.dataset.px*1);
          }
      }
  }
}());



