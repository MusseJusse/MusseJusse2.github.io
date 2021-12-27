var randomColour = "#" + ((1 << 24) * Math.random() | 0).toString(16);
document.documentElement.style.setProperty('--bgcolour', randomColour);