"use strict";
$(function () {
    var demo_idx = DEMO_IDX;
    var active_name = 'demo_' + demo_idx;
    var $active_a = $('a[name='+ active_name +']');
    $active_a.addClass('active');
    $active_a.closest('ul.left-nav-bar').show();
    $active_a.closest('ul.left-nav-bar').addClass('open');

    $('.left-nav-title').click(function () {
        var $nav_bar = $(this).siblings('ul.left-nav-bar');
        $nav_bar.slideToggle();
        if($nav_bar.hasClass('open')) {
            $nav_bar.removeClass('open');
        }else {
            var $open_nav_bar = $('ul.left-nav-bar.open');
            if($open_nav_bar) {
                $open_nav_bar.removeClass('open');
                $open_nav_bar.slideUp();
            }
            $nav_bar.addClass('open');
        }
    });
});