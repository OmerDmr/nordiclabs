(function (jQuery) {
    "use strict";
    // Site preloader -- also uncomment the div in the header and the css style for #preloader
    jQuery(window).load(function(){
        jQuery('#preloader').fadeOut(
            'slow',
            function(){
                jQuery(this).remove();
            });
    });
    // WOW
    new WOW().init();
    $('select').selectric('open');
    // ****************
    // BG Color & Image
    jQuery('section,div,footer,header').each(function(){
        var bg_color = jQuery(this).attr("data-color");
        if(bg_color){
            jQuery(this).css("background-color", "" + bg_color + "");
        }
        var txt_color = jQuery(this).attr("data-txt-color");
        if(txt_color){
            jQuery(this).css("color", "" + txt_color + "");
        }
        var l_height = jQuery(this).attr("data-line-height");
        if(l_height){
            jQuery(this).css("line-height", "" + l_height + "");
        }
        var url = jQuery(this).attr("data-image");
        if(url){
            jQuery(this).css("background-image", "url(" + url + ")");
        }
    });
    jQuery('.count').counterUp({
        delay: 10,
        time: 1000
    });
    // Elements Offset
    if(jQuery(window).width() > 991){
        function _indOffset(){
            // left offset
            var offset_left = jQuery('.container').offset().left;
            console.log(offset_left);
            jQuery('.container._leftOffset').css('padding-left',(offset_left-15)+'px');
            jQuery('.container._rightOffset').css('padding-right',(offset_left-15)+'px');
        } _indOffset();
        var resizeHandler = function(){ _indOffset(); };
        jQuery(window).resize(resizeHandler);
        setTimeout(function() {
            _indOffset();
        }, 2000);
    }

    
    jQuery('._tabs a').click(function(e) {
        e.preventDefault();
        jQuery('._tabs a,.tabscontent .contant').removeClass('active');
        jQuery(this).addClass('active');
        jQuery(jQuery(this).attr('data-tab')).addClass('active');
        // 
    });
    jQuery('._playme ._btn').click(function(e) {
        e.preventDefault();
        jQuery('._videoPopup').fadeIn('slow');
        document.getElementById("home-video").play();
        jQuery('body').css("overflow",'hidden');
    });
    jQuery('._videoPopup ._close').click(function(e) {
        e.preventDefault();
        jQuery('._videoPopup').fadeOut('slow');
        document.getElementById("home-video").pause();
        jQuery('body').css("overflow",'auto');
    });
    jQuery('._scrolldown').click(function(e) {
        jQuery('html, body').animate({
            scrollTop: jQuery("#publishing").offset().top - 100
        }, 100);
    });
   
})(jQuery);

// $(document).ready(function () {
//     $(document).on("scroll", onScroll);
    
//     //smoothscroll
//     $('a[href^="#"]').on('click', function (e) {
//         e.preventDefault();
//         $(document).off("scroll");
        
//         $('a').each(function () {
//             $(this).removeClass('active');
//         })
//         $(this).addClass('active');
      
//         var target = this.hash,
//             menu = target;
//         $target = $(target);
//         $('html, body').stop().animate({
//             'scrollTop': $target.offset().top+2
//         }, 500, 'swing', function () {
//             window.location.hash = target;
//             $(document).on("scroll", onScroll);
//         });
//     });
// });

// function onScroll(event){
//     var scrollPos = $(document).scrollTop();
//     $('#publingcarousel div').each(function () {
//         var currLink = $(this);
//         var refElement = $(currLink.attr("href"));
//         if (refElement.position().top <= scrollPos && refElement.position().top + refElement.height() > scrollPos) {
//             $('#publingcarousel div').removeClass("active");
//             currLink.addClass("active");
//         }
//         else{
//             currLink.removeClass("active");
//         }
//     });
// }
