$(document).ready(function(){
           	var bodyBgs = new Array(5);
       	 	bodyBgs[0] = "../images/dbg/dbg1.jpg";
        	bodyBgs[1] = "../images/dbg/dbg2.jpg";
        	bodyBgs[2] = "../images/dbg/dbg3.jpg";
        	bodyBgs[3] = "../images/dbg/dbg4.jpg";
        	bodyBgs[4] = "../images/dbg/dbg5.jpg";

        	var randomBgIndex = Math.round( Math.random() * 4 );

    //输出随机的背景图
        	$("img").attr({
        		"src":bodyBgs[randomBgIndex]
        	});
       
    //]]>
    
})