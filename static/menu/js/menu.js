;(function () {
    const audio = document.querySelector(`#sound`);
    const blocks = document.getElementsByClassName('a');
    for (let block of blocks) {
        block.onmouseover = () => audio.play();
    }
})();
