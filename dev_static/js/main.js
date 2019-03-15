$(function () {
    $('body').css('margin-bottom', $('.footer').outerHeight());
});

$(function () {
    $(".zoom-image").SmartPhoto();
});

$(document).ready(function(){
    $(".dropdown").hover(            
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop( true, true ).slideDown("fast");
            $(this).toggleClass('open');        
        },
        function() {
            $('.dropdown-menu', this).not('.in .dropdown-menu').stop( true, true ).slideUp("fast");
            $(this).toggleClass('open');       
        }
    );
});

$(function () {
    'use strict'
    $('[data-toggle="offcanvas"]').on('click', function () {
        $('.offcanvas-collapse').toggleClass('open')
    })
})

$(function() {
    Stickyfill.add($('.sticky'));
});

$(document).ready(function(){
    if ($(window).scrollTop() > 0 ) {
        $('.sticky').addClass('sticky-now')
    }
    else {
        $('.sticky').removeClass('sticky-now')
    }
});

$(document).ready(function(){
    $(window).scroll(function() {
        if ($(window).scrollTop() > $('.sticky').scrollTop()) {
            $('.sticky').addClass('sticky-now');
        }
        else {
            $('.sticky').removeClass('sticky-now')
        }
    });
});

$(document).ready(function(){
    $(window).scroll(function(){
        if ($(this).scrollTop() > 500) {
            $('.scroll-to-top').fadeIn(200);
        } 
        else {
            $('.scroll-to-top').fadeOut(200);
        }
    });
    $('.scroll-to-top').click(function(){
        $('html, body').animate({scrollTop : 0},300);
        return false;
    });
});

$(document).ready(function(){
    if (window.matchMedia('(min-width: 768px)').matches) {
        $('.article-item-img').matchHeight({
            byRow:false
        });
    }
});

$(document).ready(function(){
    if (window.matchMedia('(min-width: 768px)').matches) {
        $(function() {
            $('.article-item').matchHeight({
                byRow:false
            });
        });
    }
});

$('.single-item').slick({
    dots:true,
    adaptiveHeight: true
});

(function() {
    'use strict';
    window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();