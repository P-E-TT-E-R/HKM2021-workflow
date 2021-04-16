adapt();

//adapt's the height of the page to the height of the window
function adapt() {
    body = document.getElementsByTagName("body")[0];
    if (body.clientHeight < window.innerHeight) {
        body.style.minHeight = window.innerHeight + "px";
    }
}