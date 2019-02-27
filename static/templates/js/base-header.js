window.onload = function() {
    function $(id) {
        return document.getElementById(id);
    }

    function $c(siteClass) {
        return document.getElementsByClassName(siteClass);
    }

    function $s(siteSelector) {
        return document.querySelector(siteSelector);
    }

    let headerMenu = $s('div.header-menu');
    let hiddenMenu = $s('div.hidden-menu');
    let arrowMenu = $('arrow');

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    function hidden () {
        hiddenMenu.style.display = 'none';
        arrowMenu.innerHTML = "▼"
    }

    function visible () {
        hiddenMenu.style.display = 'block';
        arrowMenu.innerHTML = "▲"
    }

    addEventListener('click', function(e) {
        if (e.target === headerMenu) {
            if (hiddenMenu.style.display === 'block') hidden();
            else visible();
        } else if (e.target !== hiddenMenu) {
            hidden();
        }
    })
};