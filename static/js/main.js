jQuery(function ($) {
    'use strict';

    // Preloader

    mobileDropdown ();
    function mobileDropdown () {
      if($('.navbar-nav, .categorie-menu').length) {
        $('.sg-dropdown').append(function () {
          return '<span class="icon fa-solid fa-chevron-down "></span>';
        });
        $('.sg-dropdown .icon').on('click', function () {
          $(this).parent('li').children('ul, .sg-dropdown-menu').slideToggle();
        });
      }
    }

    // -------------------------------------------------------------
    //  Toggle Menu
    // -------------------------------------------------------------


    $("body").on("click", ".sg-toggle", function(e) {
        e.preventDefault();
        $('body').toggleClass( "sidebar-active" );
        $(this).toggleClass( "active" ); 
    });

    $("body").on("click", "#close-menu, .header-right h2", function(e) {
        e.preventDefault();
        $('body').toggleClass( "sidebar-active" );
        $(this).toggleClass( "active" ); 
    });

    $("body").on("click", ".c-toggle", function(e) {
        e.preventDefault();
        $('body').toggleClass( "cart-active" );
        $(this).toggleClass( "active" ); 
    });    

    // -------------------------------------------------------------
    //  header
    // -------------------------------------------------------------

    $(window).on('scroll',function(){
        scroll = $(window).scrollTop();
        if(scroll >50){
            $('.header-bottom').addClass('fixed-top');
            $('.sg-topbar').slideUp();
        }else{
            $('.header-bottom').removeClass('fixed-top');
            $('.sg-topbar').fadeIn();
        }
    });

    // -------------------------------------------------------------
    //  Slick Slider
    // -------------------------------------------------------------  

    $(".brand-slider").slick({
        infinite: false,
        dots: false,
        arrows: false,
        slidesToShow: 6,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 481,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    });

    $(".recent-product-slider").slick({
        infinite: false,
        dots: false,
        arrows: false,
        slidesToShow: 8,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 476,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    }); 

    $(".product-slider-1").slick({
        infinite: false,
        dots: false,
        arrows: true,
        slidesToShow: 1,
        autoplay:false,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        nextArrow: '<span class="fa-solid fa-chevron-right"></span>',
        prevArrow: '<span class="fa-solid fa-chevron-left"></span>',
    });

    $(".product-slider-2").slick({
        infinite: false,
        dots: true,
        arrows: false,
        slidesToShow: 4,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        nextArrow: '<span class="fa-solid fa-chevron-right"></span>',
        prevArrow: '<span class="fa-solid fa-chevron-left"></span>',
        responsive: [
        {
          breakpoint: 1680,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 481,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    });

    $(".product-slider").slick({
        infinite: false,
        dots: false,
        arrows: true,
        slidesToShow: 6,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        nextArrow: '<span class="fa-solid fa-angle-right arrow-right"></span>',
        prevArrow: '<span class="fa-solid fa-angle-left arrow-left"></span>',
        responsive: [
        {
          breakpoint: 1680,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 481,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    });

    $(".gallery-slider").slick({
        infinite: false,
        dots: true,
        arrows: false,
        slidesToShow: 1,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,        
    }); 

    $(".testimonial-slider").slick({
        infinite: false,
        dots: true,
        arrows: false,
        slidesToShow: 1,
        autoplay:true,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,        
    }); 

    $('.details-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        asNavFor: '.slider-nav'
    });
    
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.details-slider',
        dots: false,
        arrows: true,
        centerMode: true,
        focusOnSelect: true,
        nextArrow: '<span class="fa-solid fa-chevron-right"></span>',
        prevArrow: '<span class="fa-solid fa-chevron-left"></span>',
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 4,
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 4,
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 400,
          settings: {
            slidesToShow: 2,
          }
        }
        ]        
    });

    $(".convenience-slider").slick({
        infinite: false,
        dots: false,
        arrows: false,
        slidesToShow: 4,
        autoplay:false,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        nextArrow: '<span class="fa-solid fa-chevron-right"></span>',
        prevArrow: '<span class="fa-solid fa-chevron-left"></span>',
        responsive: [
        {
          breakpoint: 1380,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    });   

    $(".convenience-slider-1").slick({
        infinite: false,
        dots: false,
        arrows: false,
        slidesToShow: 4,
        autoplay:false,
        autoplaySpeed: 1000, 
        speed: 1000,
        pauseOnHover:true,
        slidesToScroll: 1,
        nextArrow: '<span class="fa-solid fa-chevron-right"></span>',
        prevArrow: '<span class="fa-solid fa-chevron-left"></span>',
        responsive: [
        {
          breakpoint: 1380,
          settings: {
            slidesToShow:4,
          }
        },
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
          }
        }
        ]         
    });     

    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
      $('.slick-slider').slick('setPosition');
    })

    // -------------------------------------------------------------
    //  Countdown
    // -------------------------------------------------------------             
  
    $(".countdown").countdown({
        date: "25 dec 2025 12:00:00",
        format: "on"
    });

    // -------------------------------------------------------------
    //  tab view change
    // -------------------------------------------------------------

     $('.sg-filter .list-view-tab').on('click', function() {
        $('.sg-filter .list-view-tab').addClass('active');
        $('.sg-filter .grid-view-tab').removeClass('active');
        $('.sg-filter').removeClass('grid-view-tab').addClass('list-view-tab');
    });    
  
    $('.sg-filter .grid-view-tab').on('click', function() {
        $('.sg-filter .grid-view-tab').addClass('active');
        $('.sg-filter .list-view-tab').removeClass('active');
        $('.sg-filter').removeClass('list-view-tab').addClass('grid-view-tab');
    });

    // -------------------------------------------------------------
    //  Tags input
    // -------------------------------------------------------------

    console.clear();

    $(function() {
      $('input').on('change', function(event) {

        var $element = $(event.target);
        var $container = $element.closest('.example');

        if (!$element.data('tagsinput'))
          return;

        var val = $element.val();
        if (val === null)
          val = "null";
        var items = $element.tagsinput('items');
        console.log(items[items.length - 1]);

        $('code', $('pre.val', $container)).html(($.isArray(val) ? JSON.stringify(val) : "\"" + val.replace('"', '\\"') + "\""));
        $('code', $('pre.items', $container)).html(JSON.stringify($element.tagsinput('items')));

        console.log(val);
        console.log(items);
        console.log(JSON.stringify(val));
        console.log(JSON.stringify(items));

        console.log(items[items.length - 1]);

      }).trigger('change');
    });

    $("#button").click(function() {
      var input = $("input[name='tags']").tagsinput('items');
      console.clear();
      console.log(input);
      console.log(JSON.stringify(input));
      console.log(input[input.length - 1]);
    });



    // -------------------------------------------------------------
    //  Sticky Mobile Nav
    // -------------------------------------------------------------
    
    $(window).on("scroll", function(){
        var navbar = $('.sticky-sm-menu');
        var $this = $(this);

        if($this.scrollTop() > 50) {
            navbar.addClass('menu-bg');
        }
        else {
            navbar.removeClass('menu-bg');
        }
    });

    var new_scroll_position = 0;
    var last_scroll_position;
    var trNavbar = document.getElementById("sm_menu");

    window.addEventListener('scroll', function(e) {
        last_scroll_position = window.scrollY;

        // Scrolling down
        if (new_scroll_position < last_scroll_position && last_scroll_position > 80) {
            trNavbar.classList.remove("slideUp");
            trNavbar.classList.add("slideDown");

        // Scrolling up
        } else if (new_scroll_position > last_scroll_position) {
            trNavbar.classList.remove("slideDown");
            trNavbar.classList.add("slideUp");
        }

      new_scroll_position = last_scroll_position;
    });  


$ (window).ready (function () {
  setTimeout (function () {
    $ ('#sg-modal').modal ("show")
  }, 1000)
});   


$('select').each(function(){
    var $this = $(this), numberOfOptions = $(this).children('option').length;
  
    $this.addClass('select-hidden'); 
    $this.wrap('<div class="select"></div>');
    $this.after('<div class="select-styled"></div>');

    var $styledSelect = $this.next('div.select-styled');
    $styledSelect.text($this.children('option').eq(0).text());
  
    var $list = $('<ul />', {
        'class': 'select-options'
    }).insertAfter($styledSelect);
  
    for (var i = 0; i < numberOfOptions; i++) {
        $('<li />', {
            text: $this.children('option').eq(i).text(),
            rel: $this.children('option').eq(i).val()
        }).appendTo($list);
    }
  
    var $listItems = $list.children('li');
  
    $styledSelect.click(function(e) {
        e.stopPropagation();
        $('div.select-styled.active').not(this).each(function(){
            $(this).removeClass('active').next('ul.select-options').hide();
        });
        $(this).toggleClass('active').next('ul.select-options').toggle();
    });
  
    $listItems.click(function(e) {
        e.stopPropagation();
        $styledSelect.text($(this).text()).removeClass('active');
        $this.val($(this).attr('rel'));
        $list.hide();
    });
  
    $(document).click(function() {
        $styledSelect.removeClass('active');
        $list.hide();
    });

}); 

      
    /*==============================================================*/
    // Send Email
    /*==============================================================*/ 

    $('#contactform').submit(function (e) {
        $('.flashinfo').hide();
        e.preventDefault();
    })
    .validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            phoneNumber: {
                digits: true,
                required: true,
                minlength: 5,
                maxlength: 12
            },
            name: {
                required: true,
                minlength: 5
            },
            subject: {
                required: true,
                minlength: 10
            },
            message: {
                required: true,
                minlength: 10
            }
        },
        messages: {
            email: {
                required: 'Check your email input '
            },
            name: {
                required: 'Please check your first name input'
            },
            subject: {
                required: 'Please check your message subject input'
            },
            message: {
                required: 'Please write something for us'
            }
        },
        submitHandler: function (form) {
            $.ajax({
                type: "POST",
                url: "https://mailpostexample.herokuapp.com/",
                data: $(form).serialize(),
                beforeSend: function () {
                    $('.flashinfo').hide();
                    $('.btn-l').html('Sending...')
                    $('input, textarea').attr('readonly', "readonly");
                },
                success: function (msg) {
                    if (msg == 'your message send') {
                        $('#contactform').trigger("reset");
                        $('.btn-l').html('Send Now')
                        $('input, textarea').removeAttr('readonly');
                        $('.flashinfo').show();
                        $('.flashinfo').html('Your message has been sent, I will reply to you shortly');
                    } else {
                        $('input, textarea').removeAttr('readonly');
                        $('#contactform').trigger("reset");
                        $('.flashinfo').show();
                        $('.flashinfo').html('<span>report_problem</span>something unknown error');
                    }
                }
            });
            return false;
        }
    });

// script end
});


