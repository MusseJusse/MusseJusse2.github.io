//var randomColour = "#" + ((1 << 24) * Math.random() | 0).toString(16);

var randomColour = "hsla(" + ~~(360 * Math.random()) + "," + "70%," + "80%,1)"
document.documentElement.style.setProperty('--bgcolour', randomColour);