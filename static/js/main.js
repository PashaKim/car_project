!function(t){"use strict";setTimeout((function(){t("#spinner").length>0&&t("#spinner").removeClass("show")}),1),(new WOW).init(),t(window).scroll((function(){t(this).scrollTop()>300?t(".sticky-top").css("top","0px"):t(".sticky-top").css("top","-100px")}));const o=t(".dropdown"),e=t(".dropdown-toggle"),n=t(".dropdown-menu"),i="show";t(window).on("load resize",(function(){this.matchMedia("(min-width: 992px)").matches?o.hover((function(){const o=t(this);o.addClass(i),o.find(e).attr("aria-expanded","true"),o.find(n).addClass(i)}),(function(){const o=t(this);o.removeClass(i),o.find(e).attr("aria-expanded","false"),o.find(n).removeClass(i)})):o.off("mouseenter mouseleave")})),t(document).ready((function(){t(".back-to-top").hide(),t(window).scroll((function(){t(this).scrollTop()>300?t(".back-to-top").fadeIn(100):t(".back-to-top").fadeOut(100)})),t(".back-to-top").click((function(){return t("html, body").animate({scrollTop:0},{duration:400,easing:"swing"}),!1}))})),t('[data-toggle="counter-up"]').counterUp({delay:10,time:2e3}),t(".date").datetimepicker({format:"L"}),t(".time").datetimepicker({format:"LT"}),t(".testimonial-carousel").owlCarousel({autoplay:!0,smartSpeed:1e3,center:!0,margin:25,dots:!0,loop:!0,nav:!1,responsive:{0:{items:1},768:{items:2},992:{items:3}}})}(jQuery);