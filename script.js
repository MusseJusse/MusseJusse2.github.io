var colours = new Array(6);

function search_func(e) {
    e = e || window.event;
    if (e.keyCode == 13) {
        document.getElementById('button').click();
        return false;
    }
    return true;
}

window.onload = function() {
    document.getElementById("search").focus();
  };

function getHSLAColour(h, s, l, a) {
    return `hsl(${h}, ${s}%, ${l}%, ${a})`;
}

function getColour(h) {
    var s = 70;
    var l = 80;
    var a = 1;

    return {
        h,
        hslaValue: getHSLAColour(h, s, l, a)
    }
}

colours[0] = getColour(360 * Math.random());

for (let i = 1; i < colours.length; i++) {
    colours[i] = getColour(colours[i - 1].h - 60, 70, 80, 1);
}

document.documentElement.style.setProperty('--bgcolour1', colours[0].hslaValue);
document.documentElement.style.setProperty('--bgcolour2', colours[1].hslaValue);
document.documentElement.style.setProperty('--bgcolour3', colours[2].hslaValue);
document.documentElement.style.setProperty('--bgcolour4', colours[3].hslaValue);
document.documentElement.style.setProperty('--bgcolour5', colours[4].hslaValue);
document.documentElement.style.setProperty('--bgcolour6', colours[5].hslaValue);