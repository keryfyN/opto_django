$(document).ready(function(){

    var $hoverNav = $('.bg');

    $(window).scroll(function() {
    // 100 = The point you would like to fade the nav in.

        if ($(window).scrollTop() > 100 ){
            $hoverNav.addClass('show');
        }
        else{
            $hoverNav.removeClass('show');
        }
    });
});//*end of document.ready*/


