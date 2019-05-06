(function() {
    'use strict';
    let shadow = document.getElementById('shadow');
    let requestComplete = document.getElementById('request-complete');
    let buttonRequest = document.getElementsByClassName('request');
    let requestForm = document.getElementById('request-form');
    let submitRequest = document.getElementById('submit-request');
    let login = document.getElementById('login');
    let params = document.getElementById('login-params');
    let arrow = document.getElementById('arrow');
    let enter = document.getElementsByClassName('login-params enter')[0];
    let create = document.getElementsByClassName('login-params create')[0];
    let shadowLogin = document.getElementById('shadow-login');
    let shadowRegistration = document.getElementById('shadow-create-acc');
    let errorLogin = document.getElementById('error');

    if (document.documentMode || /Edge/.test(navigator.userAgent)) {
        window.scrollTo(0, requestComplete.getBoundingClientRect().top);
    } else window.scrollBy(0, requestComplete.getBoundingClientRect().y);

    if (errorLogin.style.display === 'block') shadowLogin.style.display = 'block';

    addEventListener('scroll', function() {
        if (buttonRequest[0].getBoundingClientRect().y - requestForm.getBoundingClientRect().y > 200) {
            buttonRequest[0].style.width = '180px';
            buttonRequest[0].innerHTML = 'Отправить';
        } else {
            buttonRequest[0].style.width = '280px';
            buttonRequest[0].innerHTML = 'Написать запрос';
        }
        if (document.documentMode || /Edge/.test(navigator.userAgent)) {
            if (buttonRequest[0].getBoundingClientRect().top - requestForm.getBoundingClientRect().top > 200) {
                buttonRequest[0].style.width = '180px';
                buttonRequest[0].innerHTML = 'Отправить';
            } else {
                buttonRequest[0].style.width = '280px';
                buttonRequest[0].innerHTML = 'Написать запрос';
            }
        }
    });

    buttonRequest[0].onclick = function () {
        if (buttonRequest[0].innerText === 'Написать запрос') {
            window.scrollTo({
                top: 5000,
                behavior: "smooth",
            });
        } else if (buttonRequest[0].innerText === 'Отправить') {
            submitRequest.click();
        }
        if (document.documentMode || /Edge/.test(navigator.userAgent)) {
            if (buttonRequest[0].innerText === 'Написать запрос') {
                var scroll = setInterval(function() {
                    window.scrollBy(0, 500);
                    if (window.pageYOffset > 4500) {
                        clearInterval(scroll)
                    }
                }, 30);
            } else if (buttonRequest[0].innerText === 'Отправить') {
                submitRequest.click();
            }
        }

    };
    function hiddenParams () {
        params.style.display = "none";
        shadow.style.display = 'none';
        arrow.innerText = '▾'
    }

    function visibleParams () {
        params.style.display = "block";
        shadow.style.display = 'block';
        arrow.innerText = '▴'
    }

    addEventListener('click', function(e){
        if (e.target === login) {
            if (params.style.display === 'block') hiddenParams();
            else visibleParams();
        } else if (e.target !== params) {
            hiddenParams();
        }
        if (e.target === enter) shadowLogin.style.display = 'block';
        if (e.target === create) shadowRegistration.style.display = 'block';
        if (e.target === shadowLogin) shadowLogin.style.display = 'none';
        if (e.target === shadowRegistration) shadowRegistration.style.display = 'none';
    });
}());