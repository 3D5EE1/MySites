;(function () {
	let target;
    const info = document.querySelectorAll(`p`);
	const mySites = document.querySelectorAll('a');
    for (let site of mySites) {
    	site.onmouseover = function () {
            for (let inf of info) {
                if (site.dataset.img === inf.dataset.img) {
					inf.style.display = 'inline';
				target = inf;
                }
			}
		}
		site.onmouseout = () => target.style.display = 'none';
    }
})();
