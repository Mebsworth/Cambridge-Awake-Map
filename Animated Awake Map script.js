$(document).ready(function(){

 

$("#pause").click(function(){
  save = time;
  pause = true;
    $("#pause").css("background-color","#999999");
    $("#pause").css("color","#FFFFFF");
    $("#resume").css("background-color","#FFFFFF");
    $("#resume").css("color","#000000");
});
$("#pause").hover(
  function(){
    $("#pause").css("font-weight","bold");
},function(){
  $("#pause").css("font-weight","normal");
});

$("#resume").click(function(){
  time=save;
  pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
  animate();
});
$("#resume").hover(
  function(){
    $("#resume").css("font-weight","bold");
},function(){
  $("#resume").css("font-weight","normal");
})

	
	$('#sund').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
		$('#sund').css("background-color","#999999");
    $('#sund').css("color","#FFFFFF");
		$('#mon,#tues,#wed,#thurs,#fri,#sat').css("background-color","#FFFFFF");
    $('#mon,#tues,#wed,#thurs,#fri,#sat').css("color","#000000");
    day="sund";
    time=0;
    animate();

  });
  $('#sund').hover(
    function(){
      $('#sund').css("font-weight","bold");
    },function(){
      $('#sund').css("font-weight","normal");
    // $('#sun').css("background-color","#FFFFFF");
    // $('#sun').css("color","#000000");
  });
  $('#mon').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#mon').css("background-color","#999999");
    $('#mon').css("color","#FFFFFF");
    $('#sund,#tues,#wed,#thurs,#fri,#sat').css("background-color","#FFFFFF");
    $('#sund,#tues,#wed,#thurs,#fri,#sat').css("color","#000000");
    day="mon";
    time=0;
    animate();
  });
   $('#mon').hover(
    function(){
      $('#mon').css("font-weight","bold");
    },function(){
      $('#mon').css("font-weight","normal");
  });
  $('#tues').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#tues').css("background-color","#999999");
    $('#tues').css("color","#FFFFFF");
    $('#sund,#mon,#wed,#thurs,#fri,#sat').css("background-color","#FFFFFF");
    $('#sund,#mon,#wed,#thurs,#fri,#sat').css("color","#000000");
    day="tues";
    time=0;
    animate();
  });
   $('#tues').hover(
    function(){
      $('#tues').css("font-weight","bold");
    },function(){
      $('#tues').css("font-weight","normal");
  });
  $('#wed').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#wed').css("background-color","#999999");
    $('#wed').css("color","#FFFFFF");
    $('#mon,#tues,#sund,#thurs,#fri,#sat').css("background-color","#FFFFFF");
    $('#mon,#tues,#sund,#thurs,#fri,#sat').css("color","#000000");
    day="wed";
    time=0;
    animate();
  });
   $('#wed').hover(
    function(){
      $('#wed').css("font-weight","bold");
    },function(){
      $('#wed').css("font-weight","normal");
  });
  $('#thurs').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#thurs').css("background-color","#999999");
    $('#thurs').css("color","#FFFFFF");
    $('#mon,#tues,#wed,#sund,#fri,#sat').css("background-color","#FFFFFF");
    $('#mon,#tues,#wed,#sund,#fri,#sat').css("color","#000000");
    day="thurs";
    time=0;
    animate();
  });
   $('#thurs').hover(
    function(){
      $('#thurs').css("font-weight","bold");
    },function(){
      $('#thurs').css("font-weight","normal");
  });
  $('#fri').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#fri').css("background-color","#999999");
    $('#fri').css("color","#FFFFFF");
    $('#mon,#tues,#wed,#thurs,#sun,#sat').css("background-color","#FFFFFF");
    $('#mon,#tues,#wed,#thurs,#sun,#sat').css("color","#000000");
    day="fri";
    time=0;
    animate();
  });
   $('#fri').hover(
    function(){
      $('#fri').css("font-weight","bold");
    },function(){
      $('#fri').css("font-weight","normal");
  });
  $('#sat').click(function(){
    pause = false;
  $("#resume").css("background-color","#999999");
  $("#resume").css("color","#FFFFFF");
  $("#pause").css("background-color","#FFFFFF");
  $("#pause").css("color","#000000");
    $('#sat').css("background-color","#999999");
    $('#sat').css("color","#FFFFFF");
    $('#sund,#mon,#tues,#wed,#thurs,#fri').css("background-color","#FFFFFF");
    $('#sund,#mon,#tues,#wed,#thurs,#fri').css("color","#000000");
    day="sat";
    time=0;
    animate();
  });
   $('#sat').hover(
    function(){
      $('#sat').css("font-weight","bold");
    },function(){
      $('#sat').css("font-weight","normal");
  });

}); //document.ready