  $('.button-collapse').sideNav({
    menuWidth: 300, // Default is 300
    edge: 'left', // Choose the horizontal origin
    closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
    draggable: true // Choose whether you can drag to open on touch screens
  });
  $(document).ready(function () {
    $('.parallax').parallax();
  });
  $('#tohash').on('click', function () {
    $('html, body').animate({
      scrollTop: $(this.hash).offset().top - 5
    }, 1000);
    return false;
  });
     $("#formValidate").validate({
        rules: {
            uname: {
                required: true,
                minlength: 5
            },
            cemail: {
                required: true,
                email:true
            },
            password: {
				required: true,
				minlength: 5
			},
			cpassword: {
				required: true,
				minlength: 5,
				equalTo: "#password"
			},
			curl: {
                required: true,
                url:true
            },
            crole:"required",
            ccomment: {
				required: true,
				minlength: 15
            },
            cgender:"required",
			cagree:"required",
        },
        //For custom messages
        messages: {
            uname:{
                required: "Enter a username",
                minlength: "Enter at least 5 characters"
            },
            curl: "Enter your website",
        },
        errorElement : 'div',
        errorPlacement: function(error, element) {
          var placement = $(element).data('error');
          if (placement) {
            $(placement).append(error)
          } else {
            error.insertAfter(element);
          }
        }
     });jhh


