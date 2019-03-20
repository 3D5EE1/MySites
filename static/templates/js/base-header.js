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

    let headerMenu = $s('.header-menu'),
        hiddenMenu = $s('.hidden-menu'),
        arrowMenu = $('arrow'),
        shadow = $s('.shadow'),
        links = $S('.links'),
        cubeMenu = $('cube-menu'),
        headerLoginMenu = $s('.header-login-menu'),
        arrowLoginMenu = $('arrow-login'),
        headerBlockLogin = $s('.header-block-login')


    ;

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    function hiddenMenuSites () {
        hiddenMenu.style.display = 'none';
        shadow.style.display = 'none';
        arrowMenu.innerHTML = "▾";
        arrowMenu.style.top = '6px';
        cubeMenu.style.display = 'none';

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
        arrowMenu.innerHTML = "▴";
        arrowMenu.style.top = '4px';
        cubeMenu.style.display = 'block';

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

    let hiddenLoginMenu = function () {
        headerBlockLogin.style.display = 'none';
        shadow.style.display = 'none';
        arrowLoginMenu.innerHTML = "▾";
        arrowLoginMenu.style.top = '6px';
    };

    let visibleLoginMenu = function () {
        headerBlockLogin.style.display = 'block';
        shadow.style.display = 'block';
        arrowLoginMenu.innerHTML = "▴";
        arrowLoginMenu.style.top = '4px';
    };

    let logoutMenu = function () {

    };



    addEventListener('click', function(e) {
        if (e.target === headerMenu) {
            if (hiddenMenu.style.display === 'block') hiddenMenuSites();
            else visibleMenuSites();
        } else if (e.target !== hiddenMenu) {
            hiddenMenuSites();
        }

        if (e.target === headerLoginMenu) {
            if (headerBlockLogin.style.display === 'block') hiddenLoginMenu();
            else visibleLoginMenu();
        } else if (e.target !== headerLoginMenu) {
            hiddenLoginMenu()
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