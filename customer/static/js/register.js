$(document).ready(function(){
	$(".mail-container").hide();
	$("#phone-title").css({
		'background-color': '#0479d6'
	});
	$("#phone-title").click(function(){
		$(".mail-container").hide();
		$(".phone-container").show();
		$("#mail-title").css({
			"background-color": 'white'
		});
		$("#phone-title").css({
		'background-color': '#0479d6'
	});
	})
	$("#mail-title").click(function(){
		$(".phone-container").hide();
		$(".mail-container").show();
		$("#phone-title").css({
			"background-color": 'white'
			// property2: 'value2'
		});
		$("#mail-title").css({
		'background-color': '#0479d6'
	});
	})
 	$(":checkbox").attr('checked','checked');
 	$(":checkbox").click(function() {
    
     if($(this).is(':checked'))
   {
   	$(":submit").removeAttr('disabled');
    
   }
   else
   {
    $(":submit").attr('disabled','true');
   }
  });

})