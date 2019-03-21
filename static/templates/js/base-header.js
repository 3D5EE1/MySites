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
        headerBlockLogin = $s('.header-block-login'),
        headerLogoutMenu = $s('.header-logout-menu'),
        arrowLogoutMenu = $('arrow-logout'),
        headerBlockLogout = $s('.header-block-logout');

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    function hiddenLinks () {
        for (let i of links) {
            i.style.color = '#b8b8b8';
            i.onmouseover = function () {
                this.style.color = '#ffda1e';
                if (i === headerLoginMenu) {
                    headerLoginMenu.style.color = '#e0e1e1';
                    arrowLoginMenu.style.color = '#e0e1e1';
                }
                if (i === headerLogoutMenu) {
                    headerLogoutMenu.style.color = '#e0e1e1';
                    arrowLogoutMenu.style.color = '#e0e1e1';
                }
            };
            i.onmouseout = function () {
                this.style.color = '#b8b8b8';
                if (i === headerLoginMenu) arrowLoginMenu.style.color = '#b8b8b8';
                if (i === headerLogoutMenu) arrowLogoutMenu.style.color = '#b8b8b8';
            }
        }
    }

    function visibleLinks () {
        for (let i of links) {
            i.style.color = '#676767';
            i.onmouseover = function () {
                this.style.color = '#ffda1e';
                if (i === headerLoginMenu) {
                    headerLoginMenu.style.color = '#ffda1e';
                    arrowLoginMenu.style.color = '#ffda1e';
                }
                if (i === headerLogoutMenu) {
                    headerLogoutMenu.style.color = '#ffda1e';
                    arrowLogoutMenu.style.color = '#ffda1e';
                }
            };
            i.onmouseout = function () {
                this.style.color = '#676767';
                if (i === headerLogoutMenu) arrowLogoutMenu.style.color = '#676767';
            }
        }
    }

    function hiddenMenuSites () {
        hiddenMenu.style.display = 'none';
        shadow.style.display = 'none';
        arrowMenu.innerHTML = "▾";
        arrowMenu.style.top = '6px';
        cubeMenu.style.display = 'none';
        hiddenLinks();
    }

    function visibleMenuSites () {
        hiddenMenu.style.display = 'block';
        shadow.style.display = 'block';
        arrowMenu.innerHTML = "▴";
        arrowMenu.style.top = '4px';
        cubeMenu.style.display = 'block';
        visibleLinks();
    }

    function hiddenLinksProfile () {
        headerMenu.style.color = '#676767';



    }

    let hiddenLoginMenu = function () {
        headerBlockLogin.style.display = 'none';
        shadow.style.display = 'none';
        arrowLoginMenu.innerHTML = "▾";
        arrowLoginMenu.style.top = '6px';
        hiddenLinksProfile();
    };

    let visibleLoginMenu = function () {
        headerBlockLogin.style.display = 'block';
        shadow.style.display = 'block';
        arrowLoginMenu.innerHTML = "▴";
        arrowLoginMenu.style.top = '4px';
    };

    let hiddenLogoutMenu = function () {
        headerBlockLogout.style.display = 'none';
        shadow.style.display = 'none';
        arrowLogoutMenu.innerHTML = "▾";
        arrowLogoutMenu.style.top = '6px';
        hiddenLinksProfile();
    };

    let visibleLogoutMenu = function () {
        headerBlockLogout.style.display = 'block';
        shadow.style.display = 'block';
        arrowLogoutMenu.innerHTML = "▴";
        arrowLogoutMenu.style.top = '4px';
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
        } else if (e.target !== headerLoginMenu && headerBlockLogin) {
            hiddenLoginMenu()
        }

        if (e.target === headerLogoutMenu) {
            if (headerBlockLogout.style.display === 'block') hiddenLogoutMenu();
            else visibleLogoutMenu();
        } else if (e.target !== headerLogoutMenu && headerLogoutMenu) {
            hiddenLogoutMenu()
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