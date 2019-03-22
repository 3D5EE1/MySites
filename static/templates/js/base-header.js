window.onload = function() {
    function $qS(Selector) {
        return document.querySelector(Selector)
    }

    function $qSA(Selector) {
        return document.querySelectorAll(Selector)
    }

    let shadow = $qS('[data-name=shadow]'),

        headerMenu = $qS('[data-name=header-menu]'),
        hiddenMenu = $qS('[data-name=hidden-menu]'),
        arrowMenu = $qS('[data-name=arrow]'),
        cubeMenu = $qS('[data-name=cube-menu]'),

        itemsMenu = $qSA('[data-items]'),

        headerLoginMenu = $qS('[data-name=header-login-menu]'),
        arrowLoginMenu = $qS('[data-name=arrow-login]'),
        headerBlockLogin = $qS('[data-name=header-block-login]'),

        headerLogoutMenu = $qS('[data-name=header-logout-menu]'),
        arrowLogoutMenu = $qS('[data-name=arrow-logout]'),
        headerBlockLogout = $qS('[data-name=header-block-logout]');

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
        hiddenMenu.className = 'hidden-menu';
        shadow.className = 'shadow';
        arrowMenu.innerHTML = "▾";
        arrowMenu.className = 'arrow-down';
        cubeMenu.className = 'cube-menu';
        headerLoginMenu.className = 'header-login-menu';
        arrowLoginMenu.className = 'arrow-login';
        for (let i of itemsMenu) i.className = '';
    }

    function visibleMenuSites () {
        hiddenMenu.className = 'hidden-menu-visible';
        shadow.className = 'shadow element-visible';
        arrowMenu.innerHTML = "▴";
        arrowMenu.className = 'arrow-up';
        cubeMenu.className = 'cube-menu element-visible';
        headerLoginMenu.className = 'header-login-menu color-shadow-profile';
        arrowLoginMenu.className = 'arrow-login color-shadow-profile';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    }

    function hiddenLinksProfile () {
        headerMenu.style.color = '#676767';



    }

    // let hiddenLoginMenu = function () {
    //     headerBlockLogin.style.display = 'none';
    //     shadow.className = 'shadow-hidden';
    //     arrowLoginMenu.innerHTML = "▾";
    //     arrowLoginMenu.style.top = '6px';
    //     hiddenLinksProfile();
    // };
    //
    // let visibleLoginMenu = function () {
    //     headerBlockLogin.style.display = 'block';
    //     shadow.className = 'shadow-visible';
    //     arrowLoginMenu.innerHTML = "▴";
    //     arrowLoginMenu.style.top = '4px';
    // };
    //
    // let hiddenLogoutMenu = function () {
    //     headerBlockLogout.style.display = 'none';
    //     shadow.className = 'shadow-hidden';
    //     arrowLogoutMenu.innerHTML = "▾";
    //     arrowLogoutMenu.style.top = '6px';
    //     hiddenLinksProfile();
    // };
    //
    // let visibleLogoutMenu = function () {
    //     headerBlockLogout.style.display = 'block';
    //     shadow.className = 'shadow-visible';
    //     arrowLogoutMenu.innerHTML = "▴";
    //     arrowLogoutMenu.style.top = '4px';
    // };



    addEventListener('click', function(e) {
        if (e.target === headerMenu) {
            if (hiddenMenu.className === "hidden-menu-visible") hiddenMenuSites();
            else visibleMenuSites();
        } else if (e.target !== hiddenMenu) {
            hiddenMenuSites();
        }

        // if (e.target === headerLoginMenu) {
        //     if (headerBlockLogin.style.display === 'block') hiddenLoginMenu();
        //     else visibleLoginMenu();
        // } else if (e.target !== headerLoginMenu && headerBlockLogin) {
        //     hiddenLoginMenu()
        // }
        //
        // if (e.target === headerLogoutMenu) {
        //     if (headerBlockLogout.style.display === 'block') hiddenLogoutMenu();
        //     else visibleLogoutMenu();
        // } else if (e.target !== headerLogoutMenu && headerLogoutMenu) {
        //     hiddenLogoutMenu()
        // }
    });

    addEventListener('scroll', function(){
        if (window.pageYOffset > 38 && hiddenMenu.className === "hidden-menu-visible") {
            hiddenMenu.className = 'hidden-menu-visible hidden-menu-fixed';
        }
        if (window.pageYOffset < 38 && hiddenMenu.className === 'hidden-menu-visible hidden-menu-fixed') {
            hiddenMenu.className = 'hidden-menu-visible';
        }
    });
};