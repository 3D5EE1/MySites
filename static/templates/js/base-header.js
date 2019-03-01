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
    let shadow = $s('div.shadow');

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    function hiddenMenuSites () {
        hiddenMenu.style.display = 'none';
        shadow.style.display = 'none';
        arrowMenu.innerHTML = "˅";
    }

    function visibleMenuSites () {
        hiddenMenu.style.display = 'block';
        shadow.style.display = 'block';
        arrowMenu.innerHTML = "˄";
    }

    addEventListener('click', function(e) {
        if (e.target === headerMenu) {
            if (hiddenMenu.style.display === 'block') hiddenMenuSites();
            else visibleMenuSites();
        } else if (e.target !== hiddenMenu) {
            hiddenMenuSites();
        }
    });

    addEventListener('scroll', function(){
        if (window.pageYOffset >= 38) {
            hiddenMenu.style.position = 'fixed';
        }
        if (window.pageYOffset < 38) {
            hiddenMenu.style.position = 'relative';
        }
    });
};