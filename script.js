$('li').click(function(){
  $('ul li').removeClass('active');
  $(this).addClass('active');
  $('body').addClass('show-x');
});

$('span').click(function(){
  $('ul li.active').removeClass('active');
   $('body').removeClass('show-x');
})