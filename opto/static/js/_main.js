$(document).on('scroll', function (e) {
    $('.uk-navbar').css('opacity', ($(document).scrollTop() / 200));
});