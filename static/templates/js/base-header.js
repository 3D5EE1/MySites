window.onload = function() {
    function $qS(Selector) {
        return document.querySelector(Selector)
    }

    function $qSA(SelectorAll) {
        return document.querySelectorAll(SelectorAll)
    }

    let shadow = $qS('[data-name=shadow]'),
        headerMenu = $qS('[data-name=header-menu]'),
        hiddenMenu = $qS('[data-name=hidden-menu]'),
        arrowMenu = $qS('[data-name=arrow]'),
        cubeMenu = $qS('[data-name=cube-menu]'),

        itemsMenu = $qSA('[data-items]'),

        shadowLogin = $qS('[data-name=shadow-login]'),
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
        headerLoginMenu.className = 'header-login-menu-shadow color-shadow-profile';
        arrowLoginMenu.className = 'arrow-login color-shadow-profile';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    }

    let hiddenLoginMenu = function () {
        headerBlockLogin.className = 'header-block-login';
        shadowLogin.className = 'shadow';
        arrowLoginMenu.innerHTML = "▾";
        arrowLoginMenu.style.top = '6px';
        for (let i of itemsMenu) i.className = '';
    };

    let visibleLoginMenu = function () {
        headerBlockLogin.className = 'header-block-login-visible';
        shadowLogin.className = 'shadow element-visible';
        arrowLoginMenu.innerHTML = "▴";
        arrowLoginMenu.style.top = '4px';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    };

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
            if (hiddenMenu.className === "hidden-menu") visibleMenuSites();
            else if (hiddenMenu.className === "hidden-menu-visible") hiddenMenuSites();
        } else if (e.target !== hiddenMenu && hiddenMenu.className === "hidden-menu-visible") hiddenMenuSites();

        if (e.target === headerLoginMenu) {
            if (headerBlockLogin.className === "header-block-login") visibleLoginMenu();
            else if (headerBlockLogin.className === "header-block-login-visible") hiddenLoginMenu();
        } else if (e.target !== headerBlockLogin &&
            headerBlockLogin.className === "header-block-login-visible") hiddenLoginMenu();

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