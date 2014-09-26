$(document).ready(function(){
	$('.edit_menu').click(function(){
		$('.toolbar').toggle('slide',{direction:'right'},'slow');
	});
	$('.hide-nav').click(function(){
		$('.navbar-fixed-top').toggle('blind','slow');
		$('.hide-menu').toggle('blind','slow');
	});
});	



$(document).ready(function() {

  $('.trbox').mouseenter(function() {
       $('.glyphicon').fadeIn('fast');
          
   });
  $('.glyphicon').mouseleave(function() {
       $(this).fadeOut('fast');
   });

   $('.glyphicon').click(function() {
       $('.trbox').toggle(1000);
   }); 
});