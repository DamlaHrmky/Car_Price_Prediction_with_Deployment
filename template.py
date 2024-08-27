css = '''
html {height:100%;}
html, body {width:100%; padding:0; margin:0;}
body { 	 
	font: 11px/22px Arial, Helvetica, sans-serif;
	color:#000;
	min-width:998px;
	background: url(../images/body-bg.jpg) center 0 repeat #1c1c1c;
	height:100%;
}
.ic {border:0;float:right;background:#fff;color:#f00;width:50%;line-height:10px;font-size:10px;margin:-220% 0 0 0;overflow:hidden;padding:0}
.bg {background: url(../images/bg.jpg) center 0 repeat-y; width:100%; min-height:100%;}
.main {width:960px; margin:0 auto;}
/***********************************************************************/
a {text-decoration:none; cursor:pointer;text-decoration:none; }
a:hover {text-decoration:none;}

.button {background:#353535; display:inline-block; font-size:20px; line-height:25px; color:#fff; font-weight:bold; font-family: 'Open Sans Condensed', sans-serif; padding:9px 30px 10px 30px;}
.button:hover {background:#000;}

.button-2 {background:#fff; display:inline-block; font-size:20px; line-height:25px; color:#353535; font-weight:bold; font-family: 'Open Sans Condensed', sans-serif; padding:9px 30px 10px 30px;}
.button-2:hover {background:#000; color:#fff;}

.link {color:#0fc6ee; text-transform:uppercase; }
.link:hover {text-decoration:underline; }

.clr-1 {color:#e2e2e4;}
.text-11 {font-size:25px; line-height:42px; color:#353535; font-weight:bold; font-family: 'Open Sans Condensed', sans-serif;}
.text-1 {font-size:35px; line-height:42px; color:#353535; font-weight:bold; font-family: 'Open Sans Condensed', sans-serif;}
.text-1>strong { display:block; font-size:25px; line-height:30px; color:#9f9fa6; font-weight:bold; margin-top:-7px;}
.text-2 {font-size:14px; line-height:22px; color:#000; font-weight:bold; text-transform:uppercase;}
.text-3 {font-size:14px; line-height:22px; color:#e2e2e4; font-weight:bold; text-transform:uppercase;}

h2 { font-size:35px; line-height:42px; color:#353535; font-weight:bold; font-family: 'Open Sans Condensed', sans-serif;}

ul {margin:0; padding:0;list-style-image:none;}
ul.list-1 li {padding:0px 0 8px 15px; font-size:11px; line-height:22px; color:#fff; text-transform:uppercase; background:url(../images/marker-1.gif) 0 8px no-repeat;}
ul.list-1 li a {color:#fff;text-decoration:underline;}
ul.list-1 li a:hover {text-decoration:none;}

ul.list-2 li {padding:0px 0 8px 15px; font-size:11px; line-height:22px; color:#9f9fa6; text-transform:uppercase; background:url(../images/marker-1.gif) 0 8px no-repeat;}
ul.list-2 li a {color:#9f9fa6;text-decoration:underline;}
ul.list-2 li a:hover {text-decoration:none;}

/******************************************************************/
.clear {clear:both; line-height:0; font-size:0; width:100%;}
.wrapper {width:100%; overflow:hidden; position:relative}
.wrap {overflow:hidden; position:relative}
.extra-wrap {overflow:hidden;}
.fleft {float:left;}
.fright {float:right;}
.img-indent {float:left; margin:6px 20px 0px 0;}	
.img-indent-2 {float:left; margin:0px 20px 0px 0;}	
.img-indent-3 {float:left; margin:7px 20px 0px 0;}
.line-height {line-height:18px;}
.last {margin-right:0px !important; padding-right:0px !important;}
.align-r {text-align:right;}
.align-c {text-align:center;}
.upper {text-transform:uppercase;}

.top-1 {margin-top:23px;}
.top-2 {margin-top:20px;}
.top-3 {margin-top:33px;}
.top-4 {margin-top:27px;}
.top-5 {margin-top:23px;}

.bot-1 { padding-bottom:63px;}
.bot-2 { padding-bottom:58px;}

.p1 {margin-bottom:22px;}
.p2 {margin-bottom:7px;}
.p3 {margin-bottom:6px;}
.p4 {margin-bottom:13px;}
.p5 {margin-bottom:8px;}

/*********************************header*************************************/
header{width:100%; background:#1c1c1c;}

h1 {display:inline-block; z-index:111; float:left; padding:27px 0 0 21px;}
header p {float:right; width:230px; overflow:hidden; font:16px/20px Tahoma, Geneva, sans-serif; color:#c6c6ce; padding:27px 0 27px 0; }
header p>span {display:block; color:#fff; font-size:25px; line-height:30px; margin-top:6px;letter-spacing:-1px; }

nav {display:block; z-index:1111; position:relative; background:url(../images/header.jpg) 0 bottom repeat-x; }

ul.menu {display:block; width:960px; margin:0 auto;}
ul.menu li {float:left; display:block; height:60px; text-align:center; background:url(../images/li.jpg) right 0 no-repeat; }
ul.menu li:first-child {background:transparent;}
ul.menu li a.home {background:url(../images/home.jpg) 0 0 no-repeat;width:61px; height:60px; display:block; padding:0 !important;}
ul.menu li a { font:16px/20px Tahoma, Geneva, sans-serif; color:#000; display:block; padding:19px 22px 21px 22px; overflow:hidden; }
ul.menu li:hover, ul.menu li.current {}
ul.menu li:hover a.home, ul.menu li.current a.home {background-position:right 0;}
ul.menu li:hover a.home img, ul.menu li.current a.home img {display:none;}
ul.menu li a:hover , ul.menu li.current a {color:#0fc6ee; text-shadow:#68dcf6 0 0 5px;}


/*********************************content*************************************/
#content { width:960px; margin:0 auto; position:relative;}

.block-1 {background:#e2e2e4; border:#fff 1px solid;}
.block-2 {background:#1c1c1c;}

.pad-1 {padding:39px;}
.pad-2 {padding:30px 40px 30px 40px;}

.box-1 {overflow:hidden; padding:39px 0 39px 39px;}
.box-1>div {width:210px; float:left; margin-right:20px;}
.box-1 .text-1 {margin:10px 0 8px 0;}
.box-1 .button {margin-top:13px;}
.box-2 {width:420px; float:left; margin-right:40px; }
.box-2 h2 {margin-bottom:13px;}
.box-2>div {padding-bottom:20px;}
.box-2>div>div {position:relative; border:#494949 1px solid; background:#000; padding:18px 20px 18px 29px; color:#9f9fa6; font-style:italic; text-transform:uppercase;}
.box-2>div>div .comments-corner {position:absolute; bottom:-14px; left:29px; width:13px; height:14px; background:url(../images/comments-corner.png) 0 0 no-repeat; }
.box-2>div> a {display:inline-block; background:url(../images/icon-1.png) 0 0 no-repeat; color:#9f9fa6; font-weight:bold; text-transform:uppercase; line-height:21px; padding-top:3px; padding-left:30px; margin-top:10px;}
.box-2>div> a:hover {color:#fff;}
.box-3 {width:420px; float:left;}
.box-3 h2 {margin-bottom:16px;}
.box-3 .wrap ul.list-1 {float:left; width:190px; margin-right:40px;}
.box-3>a {margin-top:25px;}
.sub-page {background:#e2e2e4; overflow:hidden;}
.sub-page-left {border:#fff 1px solid; border-bottom:none; float:right; width:610px; padding:29px 39px 0px 39px;}
.sub-page-right {background:#1c1c1c; float:left; width:190px; padding:30px 40px 40px 40px; color:#9f9fa6;}
.sub-page-right h2 {color:#e2e2e4;}
.box-4 {overflow:hidden; text-transform:uppercase; margin:13px 0 23px 0;}
.box-4 >div {float:left; width:190px; margin-right:20px;}
.box-4 >div img {margin-bottom:13px;}
.shadow {position:relative;}
.shadow:after {content:""; position:absolute; bottom:9px; left:-40px; background:url(../images/shadow.png) 0 0 no-repeat; width:270px; height:21px;}
.box-5 img {margin:14px 0 13px 0;}
.box-5 ul {margin:8px 0 17px 0;}
.box-6 {overflow:hidden;}
.box-6 .text-2 {margin:5px 0 1px 0;}
.box-7 img {margin:13px 0 13px 0;}
.box-7 ul {margin:8px 0 0px 0;}
.box-8 img {margin:13px 0 13px 0;}
.box-9 .text-2 {margin-bottom:1px;}
.box-9 ul {margin:8px 0 0px 0;}

table {background:#fff; text-transform:uppercase; }
table td, table th {border:#e2e2e4 1px solid; border-collapse:collapse; }
table th {width:122px; font-weight:bold; text-align:left; padding:15px 10px 8px 20px;}
table td { padding:9px 10px 8px 20px;}
table td:first-child {font-weight:bold;}

/****************************footer************************/
footer {width:960px; overflow:hidden; margin:0 auto; padding:33px 0px 33px 0; background:#fff; text-align:center; color:#000; text-transform:uppercase; }

/**********************form**********************/
.map {width:190px; height:247px; margin-top:13px; }
.map iframe {width:190px; height:247px;}
dl.adr { margin-top:13px; text-transform:uppercase;}
dl.adr dt {}
dl.adr dd span { width:70px; display:block; float:left;}
dl.adr dd {white-space:nowrap;}
dl.adr dd a {}
dl.adr dd a:hover {}
#form { margin: 13px 0 0px 0px; width:610px; }
#form input {border:#fff 1px solid; background:#fff; font-size:11px; font-family:Arial, Helvetica, sans-serif; color:#000; text-transform:uppercase; padding:7px 10px 7px 18px;outline: medium none;width: 580px; height:14px; float:left;}
#form textarea {border:#fff 1px solid; background:#fff; font-size:11px; font-family:Arial, Helvetica, sans-serif; color:#000; text-transform:uppercase; height:173px;outline: medium none;overflow: auto; padding: 7px 0px 0px 18px;width:590px;resize:none;margin:0px 0 0 0;float:left;}
#form label {position:relative;display: block; min-height:35px; overflow:hidden;}
.btns {text-align:right; overflow:hidden; width:610px; padding-top:10px; }
.btns a {display:inline-block; margin-left:10px;}
'''

index = '''
<!DOCTYPE html>
<html lang="en">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Car Price Prediction</title>

<head>
<title>Car Price Prediction</title>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" media="screen" href="css/reset.css">
<link rel="stylesheet" type="text/css" media="screen" href="css/style.css">
<link rel="stylesheet" type="text/css" media="screen" href="css/slider.css">
<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:700,300' rel='stylesheet' type='text/css'>
<script src="js/jquery-1.7.min.js"></script>
<script src="js/jquery.easing.1.3.js"></script>
<script src="js/tms-0.4.1.js"></script>
<script>
$(document).ready(function () {
    $('.slider')._TMS({
        show: 0,
        pauseOnHover: true,
        prevBu: '.prev',
        nextBu: '.next',
        playBu: false,
        duration: 500,
        preset: 'fade',
        pagination: true, //'.pagination',true,'<ul></ul>'
        pagNums: false,
        slideshow: 8000,
        numStatus: false,
        banners: 'fromBottom', // fromLeft, fromRight, fromTop, fromBottom
        waitBannerAnimation: false,
        progressBar: false
    })
})
$(function () {
    if ($(window).width() <= 1066) {
        $("#slider .prev").css("left", "55px")
        $("#slider .next").css("right", "55px")
    }
})
</script>
<!--[if lt IE 9]>
<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Open+Sans+Condensed:700' rel='stylesheet' type='text/css'>
<script type="text/javascript" src="js/html5.js"></script>
<link rel="stylesheet" type="text/css" media="screen" href="css/ie.css">
<![endif]-->
</head>
<body>
<div class="bg">
  <header>
    <div class="main wrap">
      <h1><a href="index.html"><img src="images/car_price.png" alt=""></a></h1>
      
    </div>
    <nav>
      <ul class="menu">
        <li class="current"><a href="index.html" class="home"><img src="images/home.jpg" alt=""></a></li>
        <li><a href="overview.html">Overview</a></li>
        <li><a href="visualization.html">Visualization</a></li>
        <li><a href="prediction.html">Prediction</a></li>
      </ul>
      <div class="clear"></div>
    </nav>
  </header>
  <div id="slider">
    <div class="slider-block">
      <div class="slider">
        <ul class="items">
          <li><img src="images/slide-1.jpg" alt="">
            <div class="banner">
              <div><span>Statistics</span><strong>Overview of Dataset </strong>
                <p>Auto Scout data scraped from the on-line car trading company (https://www.autoscout24.com) in 2019, contains many features of 9 different car models.</p>
                <a href="overview.html" class="button">Go to Statistics</a></div> 
            </div>
          </li>
          <li><img src="images/slide-2.jpg" alt="">
            <div class="banner">
              <div><span>Visualization</span><strong>Price Analysis</strong>
                <p>Here you can review the price analysis of the vehicles with graphics and visual materials.</p>
                <a href="visualization.html" class="button">Go to Analysis</a></div>
            </div>
          </li>
          <li><img src="images/slide-3.jpg" alt="">
            <div class="banner">
              <div><span>Prediction</span><strong>Car Price Prediction</strong>
                <p>Make a price prediction for a car with the features you want by entering the necessary information.</p>
                <a href="prediction.html" class="button">Make Prediction</a></div>
            </div>
          </li>
        </ul>
      </div>
      <a href="#" class="prev"></a> <a href="#" class="next"></a> </div>
  </div>
  <section id="content">
    <div class="block-1 box-1">
      <div> <img src="images/page1-img1.jpg" alt="">
        <p class="text-11">Analyze the Cars and Their Prices </p>
        
        </div>
      <div> <img src="images/page1-1.png" alt="">
        <p class="text-11">See the Statistics of Car Prices</p>
        
         </div>
      <div> <img src="images/page1-2.png" alt="">
        <p class="text-11">Determine the Features of Your Car</p>        
        </div>

      <div class="last"> <img src="images/page1-3.png" alt="">
        <p class="text-11">Make a Price Prediction</p>
      
         </div>
    </div>
   
     
  </section>
  <footer>Car Price Prediction &copy; 2024 | <a href="#">Privacy Policy</a> | Design by: Damla Harmankaya</a></footer>
</div>
</body>

</html>
'''