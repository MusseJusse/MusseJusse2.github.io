var colours = new Array(6);

function getHSLAColor(h, s, l, a) {
    return `hsl(${h}, ${s}%, ${l}%, ${a})`;
}

function getColor(h) {
    var s = 70;
    var l = 80;
    var a = 1;

    return {
        h,
        hslaValue: getHSLAColor(h, s, l, a)
    }
}

colours[0] = getColor(360 * Math.random());

for (let i = 1; i < colours.length; i++) {
    colours[i] = getColor(colours[i - 1].h - 60, 70, 80, 1);
}

document.documentElement.style.setProperty('--bgcolour1', colours[0].hslaValue);
document.documentElement.style.setProperty('--bgcolour2', colours[1].hslaValue);
document.documentElement.style.setProperty('--bgcolour3', colours[2].hslaValue);
document.documentElement.style.setProperty('--bgcolour4', colours[3].hslaValue);
document.documentElement.style.setProperty('--bgcolour5', colours[4].hslaValue);
document.documentElement.style.setProperty('--bgcolour6', colours[5].hslaValue);