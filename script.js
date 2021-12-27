var randomColour = "hsla(" + ~~(360 * Math.random()) + "," + "70%," + "80%,1)"
document.documentElement.style.setProperty('--bgcolour', randomColour);