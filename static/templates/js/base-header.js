window.onload = function() {
    function $(id) {
        return document.getElementById(id);
    }

    function $c(siteClass) {
        return document.getElementsByClassName(siteClass);
    }

    let mySites = $c('header-menu-my-sites');

    mySites.onclick = function () {

    }

};