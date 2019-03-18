;(function() {
    function $id(id) {
        return document.getElementById(id);
    }

    let answer = $id('secret');
    const upper = $id('upper');
    const upperTarget = $id('start-policy');
    const questions = Array.from(document.querySelectorAll('.question'));
    const answers = document.querySelectorAll('.answer');

    addEventListener('scroll',function () {
        let scroll = window.pageYOffset;
        setTimeout(function(){
            if (window.pageYOffset < scroll
                && window.pageYOffset - (window.pageYOffset + upperTarget.getBoundingClientRect().y) > 0
                || (0 > window.pageYOffset - (window.pageYOffset - answer.getBoundingClientRect().y) &&
                window.pageYOffset - (window.pageYOffset - answer.getBoundingClientRect().y) > -1)) {
                upper.style.transition = 'color 1s, bottom .5s';
                upper.style.bottom = '50px';
                upper.style.animation = 'scrollUp 1s linear';
            } else if (window.pageYOffset > scroll
                || window.pageYOffset - (window.pageYOffset + upperTarget.getBoundingClientRect().y) < 0) {
                upper.style.transition = 'color 1s, bottom 1s';
                upper.style.bottom = '-50px';
                upper.style.animation = 'scrollDown 1s linear';
            }
        }, 70);
    });

    upper.onclick = () => {
        window.scrollBy({
            top: upperTarget.getBoundingClientRect().y + 71,
            behavior: 'smooth',
        });
        let up = setInterval(function(){
            if (-71 < window.pageYOffset - (window.pageYOffset - upperTarget.getBoundingClientRect().y) &&
            window.pageYOffset - (window.pageYOffset - upperTarget.getBoundingClientRect().y) < 0) {
                window.scrollBy(0, -1);
            } else if (upperTarget.getBoundingClientRect().y > 0) {
                clearInterval(up);
                window.onwheel = function() {return true;};
            }
        });
        window.onwheel = function() {return false;};
    };

    for (let question of questions) {
        question.onclick =  () => {
            answer = answers[questions.indexOf(question)];
                window.scrollTo({
                top: window.pageYOffset + answer.getBoundingClientRect().y - 70,
                behavior: "smooth",
            });
            let down = setInterval(function () {
                if (71 > window.pageYOffset - (window.pageYOffset - answer.getBoundingClientRect().y) &&
                    window.pageYOffset - (window.pageYOffset - answer.getBoundingClientRect().y) > 0) {
                    window.scrollBy(0, 1);
                } else if (answer.getBoundingClientRect().y < 0) {
                    clearInterval(down);
                    window.onwheel = function() {return true;};
                }
            }, 0);
            window.onwheel = function() {return false;};
        }
    }
}());









// (function (){
//     function $id(id) {
//         return document.getElementById(id)
//     }
//     let upper = $id('upper');
//     let upperTarget = $id('start-policy');
//     addEventListener('wheel',function () {
//         let scroll = window.pageYOffset;
//         setTimeout(function(){
//             if (window.pageYOffset < scroll) {
//                 upper.style.transition = 'color 1s, bottom 1s';
//                 upper.style.bottom = '5%';
//                 upper.style.animation = 'scrollUp 1s linear'
//             } else if (window.pageYOffset > scroll) {
//                 upper.style.transition = 'color 1s, bottom .6s';
//                 upper.style.bottom = '-5%';
//                 upper.style.animation = 'scrollDown 1s linear'
//             }
//         }, 70);
//     });
//
//     upper.onclick = () => {
//         window.scrollBy({
//             top: upperTarget.getBoundingClientRect().y + 70,
//             behavior: 'smooth',
//         });
//         let up = setInterval(function(){
//             if (-71 < window.pageYOffset - (window.pageYOffset - upperTarget.getBoundingClientRect().y) &&
//             window.pageYOffset - (window.pageYOffset - upperTarget.getBoundingClientRect().y) < 0) {
//                 window.scrollBy(0, -1);
//             } else if (upperTarget.getBoundingClientRect().y > 0) {
//                 clearInterval(up);
//                 window.onwheel = function() {return true;};
//             }
//         });
//         window.onwheel = function() {return false;};
//     }
// }());



// ;(function() {
//     const questions = Array.from(document.querySelectorAll('.question'));
//     const answers = document.querySelectorAll('.answer');
//     for (let question of questions) {
//         question.onclick = () => {
//             let answer = answers[questions.indexOf(question)];
//             window.scrollTo({
//                 top: window.pageYOffset + answer.getBoundingClientRect().y,
//                 behavior: "smooth",
//             });
//         }
//     }
// }());

 // const answers = document.querySelectorAll('.answer');
 // answers[0].getBoundingClientRect().y
 // window.pageYOffset

// ;(function() {
//     let pxDown = 0;
//     const questions = Array.from(document.querySelectorAll('.question'));
//     const answers = document.querySelectorAll('.answer');
//     let scroll = () => {
//         clearTimeout();
//         if (pxDown < 50){
//             window.scrollBy(0, 1);
//             pxDown++;
//             setInterval(scroll, 0)
//         }
//         if (pxDown === 50) {
//             return clearInterval();
//         }
//     };
//
//     for (let question of questions) {
//         question.onclick = function firstScroll() {
//             let answer = answers[questions.indexOf(question)];
//             let answerY = answer.getBoundingClientRect().y - 50;
//             if (window.pageYOffset < answerY) {
//                 window.scrollTo({
//                     top: window.pageYOffset + answerY,
//                     behavior: "smooth",
//                 });
//             setTimeout(scroll, answerY);
//             }
//         }
//     }
// }());



// (function () {
//     'use strict';
//
//     let answerY = [];
//     let speed = [13, 17, 20, 24, 28, 30, 33, 42, 47, 50];
//     let stopper = [50, 50, 60, 60, 60, 60, 80, 90, 90, 100];
//
//     const answers = document.querySelectorAll('.answer');
//     const questions = Array.from(document.querySelectorAll('.question'));
//
//     function checkYAnswers() {
//         for (let answer of answers) {
//         answerY = answerY.concat(answer.getBoundingClientRect().y);
//         }
//     }
//
//     window.onload = () => {checkYAnswers(); console.log(answerY);};
//
//     window.onresize = () => {
//         answerY = [];
//         checkYAnswers();
//         console.log(answerY);
//         console.log('resize');
//     };
//
//     for (let question of questions) {
//         question.onclick = function scroll() {
//             if (window.pageYOffset < (answerY[questions.indexOf(question)] - stopper[questions.indexOf(question)])) {
//                 window.scrollBy(0, speed[questions.indexOf(question)]);
//                 setTimeout(scroll, 0);
//             } else if (window.pageYOffset < answerY[questions.indexOf(question)]) {
//                 window.scrollBy(0, 1);
//                 setTimeout(scroll, 0);
//             }
//             if (window.pageYOffset > answerY[questions.indexOf(question)]) {
//                 window.scrollTo(0, answerY[questions.indexOf(question)] + 1);
//             }
//         }
//
//     }
// }());



// function buildTOC() {
//   var TOC = [];
//   $(".legalDocContent h1, h2, h3").each(function (i, h) {
//     var html = h.innerHTML;
//     var q = html.indexOf("?");
//     var text = ~q ? html.substr(0, q + 1) : html;
//     var id = hashCode(text);
//     var options = { class: "Button--flat" };
//
//     if (h.nodeName === "H3") {
//       options.css = { marginLeft: "1em" };
//     }
//
//     $(h).attr("id", id);
//
//     var li = $("<li/>", options).on("click", function () {
//       $("html,body").animate({ scrollTop: $('#' + id).offset().top }, {
//         duration: 850,
//         easing: "easeOutExpo",
//         done: function () {
//           setTimeout(function () {
//             fadeIn($("#backToTop"));
//           }, 750);
//         }
//       });
//     }).html(text);
//
//     TOC.push(li);
//   });
//
//   if (TOC.length > 3) {
//     $("#Toc").append(TOC);
//   } else {
//     $("#Toc").css({
//       display: "none"
//     });
//   }
// }
