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

    function $S(siteSelectors) {
        return document.querySelectorAll(siteSelectors);
    }

    let headerMenu = $s('.header-menu');
    let hiddenMenu = $s('.hidden-menu');
    let arrowMenu = $('arrow');
    let shadow = $s('.shadow');
    let links = $S('.links');

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    function hiddenMenuSites () {
        hiddenMenu.style.display = 'none';
        shadow.style.display = 'none';
        arrowMenu.innerHTML = "˅";
        for (let i of links) {
            i.style.color = '#b8b8b8';
            i.onmouseover = function () {
                this.style.color = '#ffda1e'
            };
            i.onmouseout = function () {
                this.style.color = '#b8b8b8'
            }
        }
    }

    function visibleMenuSites () {
        hiddenMenu.style.display = 'block';
        shadow.style.display = 'block';
        arrowMenu.innerHTML = "˄";
        for (let i of links) {
            i.style.color = '#676767';
            i.onmouseover = function () {
                this.style.color = '#ffda1e'
            };
            i.onmouseout = function () {
                this.style.color = '#676767'
            }
        }
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
        if (window.pageYOffset > 38) {
            hiddenMenu.style.position = 'fixed';
        }
        if (window.pageYOffset < 38) {
            hiddenMenu.style.position = 'relative';
        }
    });
};