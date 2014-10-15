$(document).ready(function() {
//hello
 $(".hello").hide();

  $(".par").click(function() {
    $(".hello").slideToggle();
  });



});

function nomfunction(arg){
  $("#"+arg+"-comment").slideToggle();
}
