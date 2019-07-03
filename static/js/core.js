window.onload = function () {
    var imgs = document.getElementsByTagName('img')
    for (var i = 0; i < imgs.length; i++) {
        imgs[i].onerror = function () {
            this.src = '/static/image/no_image.png'
        }
    }
}