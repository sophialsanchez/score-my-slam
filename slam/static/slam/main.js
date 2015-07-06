$(document).ready(function(){
	$("#start-slam-button").click(function(){
		$("#start-slam-button").hide();
		$(".slam-form").slideDown();
	});
	
	var i = 3;
	$(".add-poet").click(function(){
		i++;
		$(".poet-list").append("<p class=" + i + ">Poet #" + i + ": <input type='text'></p>");
	});
	
	$(".remove-poet").click(function(){
		if(i==2){
			alert("You need at least two poets to have a slam!");
		}
		else{
			$("." + i ).remove();
			i--;
		}
	});
	
	$(function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
  	});
  
  	$(".view-leaderboard").click(function(){
		$(".view-leaderboard").hide();
		$(".leaderboard").show();
		$(".hide-leaderboard").show();
	});
	
	$(".hide-leaderboard").click(function(){
		$(".hide-leaderboard").hide();
		$(".leaderboard").hide();
		$(".view-leaderboard").show();
	});
	

	$('a[href^="#"]').on('click',function (e) {
	    e.preventDefault();

	    var target = this.hash;
	    var $target = $(target);

	    $('html, body').stop().animate({
	        'scrollTop': $target.offset().top
	    }, 900, 'swing', function () {
	        window.location.hash = target;
	    });

});
});