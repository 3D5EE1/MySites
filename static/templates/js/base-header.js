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
        headerItems = $qS('[data-name=header-items]'),

        shadowLogin = $qS('[data-name=shadow-login]'),
        headerLoginMenu = $qS('[data-name=header-login-menu]'),
        arrowLoginMenu = $qS('[data-name=arrow-login]'),
        headerBlockLogin = $qS('[data-name=header-block-login]'),
        headerBlockLoginSize,

        headerLogoutMenu = $qS('[data-name=header-logout-menu]'),
        arrowLogoutMenu = $qS('[data-name=arrow-logout]'),
        headerBlockLogout = $qS('[data-name=header-block-logout]'),
        headerBlockLogoutSize,

        headerLanguagesMenuInactive = $qS('[data-name=header-languages-menu]'),
        svgSearchBlock = $qS('[data-name=svg-search-block]'),
        svgSearch = document.getElementById('svg-search'),
        svgLanguages = document.getElementById('svg-languages'),
        headerSearchButtonClose = $qS('[data-name=header-search-button-close]'),
        headerSearchInput = document.getElementById('header-search-input'),
        headerSearchClose = document.getElementById('header-search-close'),
        buttonSvgSearch = $qS('[data-name=button-svg-search]'),

        mobileShadow = $qS('[data-name=mobile-shadow]'),
        mobileMenuSiteButton = $qS('[data-name=mobile-menu-site-button]'),
        mobileMenuProfileButton = $qS('[data-name=mobile-menu-profile-button]'),
        headerMobileMenu = $qS('[data-name=header-mobile-menu]'),
        headerMobileProfile = $qS('[data-name=header-mobile-profile]'),
        headerMobileProfileCloser = $qS('[data-name=header-mobile-menu-profile-closer]'),
        closeMobileMenuProfileButton = $qS('[data-name=close-mobile-menu-profile-button]'),

        widthScreen = document.documentElement.clientWidth;

    // let arrowUp = document.createTextNode("▲");
    // let arrowDown = document.createTextNode("▼");
    // arrowUP.appendChild(arrowUp);

    // function hiddenLinks () {
    //     for (let i of links) {
    //         i.style.color = '#b8b8b8';
    //         i.onmouseover = function () {
    //             this.style.color = '#ffda1e';
    //             if (i === headerLoginMenu) {
    //                 headerLoginMenu.style.color = '#e0e1e1';
    //                 arrowLoginMenu.style.color = '#e0e1e1';
    //             }
    //             if (i === headerLogoutMenu) {
    //                 headerLogoutMenu.style.color = '#e0e1e1';
    //                 arrowLogoutMenu.style.color = '#e0e1e1';
    //             }
    //         };
    //         i.onmouseout = function () {
    //             this.style.color = '#b8b8b8';
    //             if (i === headerLoginMenu) arrowLoginMenu.style.color = '#b8b8b8';
    //             if (i === headerLogoutMenu) arrowLogoutMenu.style.color = '#b8b8b8';
    //         }
    //     }
    // }

    // function visibleLinks () {
    //     for (let i of links) {
    //         i.style.color = '#676767';
    //         i.onmouseover = function () {
    //             this.style.color = '#ffda1e';
    //             if (i === headerLoginMenu) {
    //                 headerLoginMenu.style.color = '#ffda1e';
    //                 arrowLoginMenu.style.color = '#ffda1e';
    //             }
    //             if (i === headerLogoutMenu) {
    //                 headerLogoutMenu.style.color = '#ffda1e';
    //                 arrowLogoutMenu.style.color = '#ffda1e';
    //             }
    //         };
    //         i.onmouseout = function () {
    //             this.style.color = '#676767';
    //             if (i === headerLogoutMenu) arrowLogoutMenu.style.color = '#676767';
    //         }
    //     }
    // }

    function hiddenMenuSites () {
        hiddenMenu.className = 'hidden-menu';
        shadow.className = 'shadow';
        arrowMenu.innerHTML = "▾";
        arrowMenu.className = 'arrow-down';
        cubeMenu.className = 'cube-menu';
        svgSearch.className.baseVal = 'svg-search';
        svgLanguages.className.baseVal = 'svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu';
        if (headerLoginMenu) headerLoginMenu.className = 'header-login-menu';
        if (arrowLoginMenu) arrowLoginMenu.className = 'arrow-login';
        if (headerLogoutMenu) headerLogoutMenu.className = 'header-logout-menu';
        if (arrowLogoutMenu) arrowLogoutMenu.className = 'arrow-logout';
        for (let i of itemsMenu) i.className = '';
    }

    function visibleMenuSites () {
        hiddenLoginMenu();
        hiddenLogoutMenu();
        hiddenMenu.className = 'hidden-menu-visible';
        shadow.className = 'shadow element-visible';
        arrowMenu.innerHTML = "▴";
        arrowMenu.className = 'arrow-up';
        cubeMenu.className = 'cube-menu element-visible';
        svgSearch.className.baseVal = 'svg-search color-shadow-svg';
        svgLanguages.className.baseVal = 'svg-languages color-shadow-svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu-inactive';
        if (headerLoginMenu) headerLoginMenu.className = 'header-login-menu-shadow color-shadow-profile';
        if (arrowLoginMenu) arrowLoginMenu.className = 'arrow-login color-shadow-profile';
        if (headerLogoutMenu) headerLogoutMenu.className = 'header-logout-menu-shadow color-shadow-profile';
        if (arrowLogoutMenu) arrowLogoutMenu.className = 'arrow-logout color-shadow-profile';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    }

    let hiddenLoginMenu = function () {
        if (headerBlockLogin) {
            headerBlockLogin.style.right = '-26px';
            headerBlockLogin.className = 'header-block-login';
        }
        shadowLogin.className = 'shadow';
        if (arrowLoginMenu) {
        arrowLoginMenu.innerHTML = "▾";
        arrowLoginMenu.className = 'arrow-login-down';
        }
        headerMenu.className = 'header-menu';
        arrowMenu.className = 'arrow-down';
        svgSearch.className.baseVal = 'svg-search';
        svgLanguages.className.baseVal = 'svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu';
        for (let i of itemsMenu) i.className = '';
    };

    let visibleLoginMenu = function () {
        headerBlockLogin.className = 'header-block-login-visible';
        headerBlockLoginSize = headerBlockLogin.getBoundingClientRect();
        shadowLogin.className = 'shadow element-visible';
        arrowLoginMenu.innerHTML = "▴";
        arrowLoginMenu.className = 'arrow-login-up';
        headerMenu.className = 'header-menu-shadow color-shadow-profile';
        arrowMenu.className = 'arrow-down color-shadow-profile';
        svgSearch.className.baseVal = 'svg-search color-shadow-svg';
        svgLanguages.className.baseVal = 'svg-languages color-shadow-svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu-inactive';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    };

    let hiddenLogoutMenu = function () {
        if (headerBlockLogout) {
            headerBlockLogout.style.right = '-26px';
            headerBlockLogout.className = 'header-block-logout';
        }
        shadowLogin.className = 'shadow';
        if (arrowLogoutMenu) {
            arrowLogoutMenu.innerHTML = "▾";
            arrowLogoutMenu.className = 'arrow-logout-down';
        }
        headerMenu.className = 'header-menu';
        arrowMenu.className = 'arrow-down';
        svgSearch.className.baseVal = 'svg-search';
        svgLanguages.className.baseVal = 'svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu';
        for (let i of itemsMenu) i.className = '';
    };

    let visibleLogoutMenu = function () {
        headerBlockLogout.className = 'header-block-logout-visible';
        headerBlockLogoutSize = headerBlockLogout.getBoundingClientRect();
        shadowLogin.className = 'shadow element-visible';
        arrowLogoutMenu.innerHTML = "▴";
        arrowLogoutMenu.className = 'arrow-logout-up';
        headerMenu.className = 'header-menu-shadow color-shadow-profile';
        arrowMenu.className = 'arrow-down color-shadow-profile';
        svgSearch.className.baseVal = 'svg-search color-shadow-svg';
        svgLanguages.className.baseVal = 'svg-languages color-shadow-svg-languages';
        headerLanguagesMenuInactive.className = 'header-languages-menu-inactive';
        for (let i of itemsMenu) i.className = 'color-shadow-profile';
    };

    let searchVisible = function () {
        svgSearchBlock.className = 'svg-search-block element-hidden';
        headerItems.className = 'header-items element-hidden';
        headerSearchInput.className = 'header-search-input';
        headerSearchButtonClose.className = 'header-search-button-close';
        if (headerSearchInput.volume === '') buttonSvgSearch.className = 'button-svg-search';
        else if (headerSearchInput.value !== '') buttonSvgSearch.className = 'button-svg-search element-visible';
    };

    let searchHidden = function () {
        svgSearchBlock.className = 'svg-search-block element-visible';
        headerItems.className = 'header-items';
        headerSearchInput.className = 'header-search-input input-search-hidden';
        headerSearchButtonClose.className = 'element-hidden';
        buttonSvgSearch.className = 'element-hidden';
    };

    headerSearchInput.oninput = function () {
        if (headerSearchInput.value !== '') buttonSvgSearch.className = 'button-svg-search element-visible';
        else buttonSvgSearch.className = 'button-svg-search';
    };

    let mobileMenuSiteVisible = function() {
        headerMobileMenu.className = 'header-mobile-menu element-visible';
        mobileShadow.className = 'mobile-shadow element-visible';
    };

    let mobileMenuSiteHidden = function() {
        headerMobileMenu.className = 'header-mobile-menu';
        mobileShadow.className = 'mobile-shadow';
    };

    let mobileMenuProfileVisible = function() {
        headerMobileProfile.className = 'header-mobile-profile-visible';
        mobileShadow.className = 'mobile-shadow element-visible';
    };

    let mobileMenuProfileHidden = function() {
        headerMobileProfile.className = 'header-mobile-profile-hidden';
        mobileShadow.className = 'mobile-shadow';
    };

    addEventListener('click', function(e) {
        if (e.target === headerMenu || e.target === arrowMenu) {
            if (hiddenMenu.className === "hidden-menu") visibleMenuSites();
            else if (hiddenMenu.className === "hidden-menu-visible") hiddenMenuSites();
        } else if ((e.target !== hiddenMenu &&
            hiddenMenu.className === "hidden-menu-visible") || e.target === shadow) hiddenMenuSites();

        if (e.target === headerLoginMenu || e.target === arrowLoginMenu) {
            if (headerBlockLogin.className === "header-block-login") visibleLoginMenu();
            else if (headerBlockLogin.className === "header-block-login-visible") hiddenLoginMenu();
        } else if ((e.target !== headerBlockLogin && headerBlockLogin &&
            headerBlockLogin.className === "header-block-login-visible") || e.target === shadowLogin) hiddenLoginMenu();

        if (e.target === headerLogoutMenu || e.target === arrowLogoutMenu) {
            if (headerBlockLogout.className === "header-block-logout") visibleLogoutMenu();
            else if (headerBlockLogout.className === "header-block-logout-visible") hiddenLogoutMenu();
        } else if (e.target !== headerBlockLogout && headerBlockLogout &&
            headerBlockLogout.className === "header-block-logout-visible" || e.target === shadowLogin) hiddenLogoutMenu();

        if (e.target === svgSearch || e.target === svgSearchBlock) searchVisible();
        else if (headerSearchInput.className === 'header-search-input' &&
            (e.target === headerSearchClose || e.target !== headerSearchInput)) searchHidden();

        if (e.target === mobileMenuSiteButton) mobileMenuSiteVisible();
        else if (e.target === mobileShadow ) mobileMenuSiteHidden();

        if (e.target === mobileMenuProfileButton ) mobileMenuProfileVisible();
        else if (e.target === mobileShadow || e.target === headerMobileProfileCloser ||
        e.target === closeMobileMenuProfileButton) mobileMenuProfileHidden();
    });

    addEventListener('scroll', function(){
        if (window.pageYOffset > 38 && hiddenMenu.className === "hidden-menu-visible") {
            hiddenMenu.className = 'hidden-menu-visible element-fixed-top';
        }
        if (window.pageYOffset < 38 && hiddenMenu.className === 'hidden-menu-visible element-fixed-top') {
            hiddenMenu.className = 'hidden-menu-visible';
        }
        if (window.pageYOffset > 38 && headerBlockLogin && headerBlockLogin.className === "header-block-login-visible") {
             headerBlockLogin.className = 'header-block-login-visible element-fixed-top';
             headerBlockLogin.style.right = document.documentElement.clientWidth - headerBlockLoginSize.right + 'px';
        }
        if (window.pageYOffset < 38 &&  headerBlockLogin &&
        headerBlockLogin.className === 'header-block-login-visible element-fixed-top') {
            headerBlockLogin.className = "header-block-login-visible";
            headerBlockLogin.style.right = '-26px'
        }
        if (window.pageYOffset > 38 && headerBlockLogout && headerBlockLogout.className === "header-block-logout-visible") {
             headerBlockLogout.className = 'header-block-logout-visible element-fixed-top';
             headerBlockLogout.style.right = document.documentElement.clientWidth - headerBlockLogoutSize.right + 'px';
        }
        if (window.pageYOffset < 38 &&  headerBlockLogout &&
        headerBlockLogout.className === 'header-block-logout-visible element-fixed-top') {
            headerBlockLogout.className = "header-block-logout-visible";
            headerBlockLogout.style.right = '-26px'
        }
    });

    addEventListener('resize', function(){
        if (widthScreen !== document.documentElement.clientWidth) {
            shadow.click();
        }
    })
};