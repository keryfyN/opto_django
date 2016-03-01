// ------ owl js ------
$(document).ready(function() {

  $("#owl-example").owlCarousel({

      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      paginationSpeed : 400,
      //singleItem:true

      // "singleItem:true" is a shortcut for:
       items : 1,
       itemsDesktop : false,
       itemsDesktopSmall : false,
       itemsTablet: false,
       itemsMobile : false,
       autoplay:true,
       loop:true,
       margin: 10,
       nav:true,
       navigationText: false,
    });

});
