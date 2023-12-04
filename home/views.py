from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    return HttpResponse("<h1> WELCOME TO DJANGO .<h1>")

def Login_Shubham (request):
    return HttpResponse("<h1> LOGIN SUCCESSFULLY ...!<h1>")

def Register_shubham (request):
    return HttpResponse("<h1> REGISTER SUCCESSFULLY ...!<h1>")


def Register (request):
    return HttpResponse(''' 
  <title>Register</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: black;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: ghostwhite;            
                        
        }

        .register-container {
            background-color: rgb(255 253 253 / 10%);
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }

        .form-group button {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="register-container">
        <h2 align='center'>Registration </h2>
                       </br> </br>
        <form action="/Register_Shubham/">

            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
                        
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
             </br> </br>
                        
            <div align='center' class="form-group">
                <button <a href="http://127.0.0.1:7000/Register_Shubham/" type="submit" align='center'> Register</button>
            </div>

                        </br>
                        
                        <p> Already have an Account ? <a href="http://127.0.0.1:7000/Login/" class="button">Login</a></p>
        </form>
    </div>
</body>
''')
# def Login (request):
#     return HttpResponse('''<h1 align='center', color='red'> LOGIN <h1>
#                         <hr>
#                         <form align= 'center'>
#                         <label for="fname">First name:</label>
#                         <input type="text" id="fname" name="fname"></br></br>
#                         <label for="lname">Last name:</label>
#                         <input type="text" id="lname" name="lname"></br>
#                         <input type="submit" value="Submit">
#                         </form>                       
                        
#                         ''')

def Login (request):
    return HttpResponse('''
          <title>Login</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: black;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: ghostwhite;
        }

        .login-container {
            background-color:rgb(255 253 253 / 10%);
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .form-group {
            margin-bottom: 15px          
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }

        .form-group button {
            background-color: #4caf50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2 align='center'> Login</h2>
        <form action="/Login_Shubham/">
        
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
                        
            <div align='center' class="form-group">
                <button <a href="http://127.0.0.1:7000/Login_Shubham/"> Login </button>
            </div>
                        
            </br></br>
            <p> Dont have an Account? <a href="http://127.0.0.1:7000/Register/"> Register </a></p>
        </form>
    </div>
    </form>
     ''')


def New_Login (request):
    return HttpResponse(''' 
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600' rel='stylesheet' type='text/css'>
<link href="//netdna.bootstrapcdn.com/font-awesome/3.1.1/css/font-awesome.css" rel="stylesheet">                                             
<style>
body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, 
pre, form, fieldset, input, textarea, p, blockquote, th, td { 
  padding:0;
  margin:0;}

fieldset, img {border:0}

ol, ul, li {list-style:none}

:focus {outline:none}

body,
input,
textarea,
select {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  color: #4c4c4c;
}

p {
  color: white;
  font-size: 14px;
  width: 230px;
  display: inline-block;
  margin-left: 18px;
}
h1 {
  font-size: 32px;
  font-weight: 300;
  color: white;
  text-align: center;
  padding-top: 10px;
  margin-bottom: 10px;
}
                        
html{
  background-color: black;
}

.testbox {
  margin: 51px auto;
  width: 343px; 
  height: 464px; 
  -webkit-border-radius: 8px/7px; 
  -moz-border-radius: 8px/7px; 
  border-radius: 8px/7px;  
  background-color: rgba(255, 255, 255, 0.1); 
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  border: solid 1px #cbc9c9;
}

form{
  margin: 0 30px;
 }

hr{
  border-color: black;
  border-width: thin;
}

input[type=text],input[type=password]{
  width: 200px; 
  height: 35px; 
  -webkit-border-radius: 0px 4px 4px 0px/5px 5px 4px 4px; 
  -moz-border-radius: 0px 4px 4px 0px/0px 0px 4px 4px; 
  border-radius: 0px 4px 4px 0px/5px 5px 4px 4px; 
  background-color: #fff; 
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  border: solid 1px #cbc9c9;
  margin-left: -5px;
  margin-top: 13px; 
  padding-left: 10px;
}

input[type=password]{
  margin-bottom: 25px;
}

input[type=text]{
  margin-top: 77px;
}

#icon {
  display: inline-block;
  width: 30px;
  background-color: #3a57af;
  padding: 10px 0px 8px 15px;
  margin-left: 15px;
  -webkit-border-radius: 4px 0px 0px 4px; 
  -moz-border-radius: 4px 0px 0px 4px; 
  border-radius: 4px 0px 0px 4px;
  color: white;
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.09);
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  border: solid 0px #cbc9c9;
}

.accounttype{
  margin-left: 8px;
  margin-top: 20px;
}

a.button {                     
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: white;
  padding: 6px 25px 0px 20px;
  margin: 10px 8px 20px 0px;
  display: inline-block;
  text-decoration: none;
  width: 230px; height: 27px; 
  -webkit-border-radius: 5px; 
  -moz-border-radius: 5px; 
  border-radius: 5px; 
  background-color: #098507; 
  -webkit-box-shadow: 0 3px rgba(58,87,175,.75); 
  -moz-box-shadow: 0 3px rgba(58,87,175,.75); 
  box-shadow: 0 3px rgba(9,133,7,1);
  transition: all 0.1s linear 0s; 
  top: 0px;
  position: relative;
}

a.button:hover {
  top: 3px;
  background-color:#098507;
  -webkit-box-shadow: none; 
  -moz-box-shadow: none; 
  box-shadow: none;
  
}                     
                                    
</style>
 
<div class="testbox">
  <h1>LOGIN</h1>

  <form action="/">
      <hr>
  <label id="icon" for="name"><i class="icon-envelope "></i></label>
  <input type="text" name="name" id="name" placeholder="Email" required/>
  
  <label id="icon" for="name"><i class="icon-shield"></i></label>
  <input type="password" name="name" id="name" placeholder="Password" required/>

   <a href="http://127.0.0.1:7000/Login_Shubham/"> class="button">LOGIN</a>
                        
                        </br></br>

   <p> Dont have an Account ? <a href="http://127.0.0.1:7000/Register/"> Register</a></p>
   
  </form>
</div>
                        
''')

def New_Register (request):
    return HttpResponse(''' 
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,300italic,400italic,600' rel='stylesheet' type='text/css'>
<link href="//netdna.bootstrapcdn.com/font-awesome/3.1.1/css/font-awesome.css" rel="stylesheet">                                             
<style>
body, div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, 
pre, form, fieldset, input, textarea, p, blockquote, th, td { 
  padding:0;
  margin:0;}

fieldset, img {border:0}

ol, ul, li {list-style:none}

:focus {outline:none}

body,
input,
textarea,
select {
  font-family: 'Open Sans', sans-serif;
  font-size: 16px;
  color: #4c4c4c;
}

p {
  color: white;
  font-size: 14px;
  width: 230px;
  display: inline-block;
  margin-left: 18px;
}
                   
h1 {
  font-size: 32px;
  font-weight: 300;
  color: white;
  text-align: center;
  padding-top: 10px;
  margin-bottom: 10px;
}

html{
  background-color: black;
}

.testbox {
  margin: 20px auto;
  width: 343px; 
  height: 464px; 
  -webkit-border-radius: 8px/7px; 
  -moz-border-radius: 8px/7px; 
  border-radius: 8px/7px; 
  background-color: rgba(255, 255, 255, 0.1); 
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.31); 
  border: solid 1px #cbc9c9;
}

input[type=radio] {
  visibility: hidden;
}

form{
  margin: 0 30px;
}

label.radio {
  cursor: pointer;
  text-indent: 35px;
  overflow: visible;
  display: inline-block;
  position: relative;
  margin-bottom: 15px;
}

label.radio:before {
  background: #3a57af;
  content:'';
  position: absolute;
  top:2px;
  left: 0;
  width: 20px;
  height: 20px;
  border-radius: 100%;
}

label.radio:after {
	opacity: 0;
	content: '';
	position: absolute;
	width: 0.5em;
	height: 0.25em;
	background: transparent;
	top: 7.5px;
	left: 4.5px;
	border: 3px solid #ffffff;
	border-top: none;
	border-right: none;

	-webkit-transform: rotate(-45deg);
	-moz-transform: rotate(-45deg);
	-o-transform: rotate(-45deg);
	-ms-transform: rotate(-45deg);
	transform: rotate(-45deg);
}

input[type=radio]:checked + label:after {
	opacity: 1;
}

hr{
  border-color: black;
  border-width: thin;
}

input[type=text],input[type=password]{
  width: 200px; 
  height: 39px; 
  -webkit-border-radius: 0px 4px 4px 0px/5px 5px 4px 4px; 
  -moz-border-radius: 0px 4px 4px 0px/0px 0px 4px 4px; 
  border-radius: 0px 4px 4px 0px/5px 5px 4px 4px; 
  background-color: #fff; 
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  border: solid 1px #cbc9c9;
  margin-left: -5px;
  margin-top: 13px; 
  padding-left: 10px;
}

input[type=password]{
  margin-bottom: 25px;
}

#icon {
  display: inline-block;
  width: 30px;
  background-color: #3a57af;
  padding: 8px 0px 8px 15px;
  margin-left: 15px;
  -webkit-border-radius: 4px 0px 0px 4px; 
  -moz-border-radius: 4px 0px 0px 4px; 
  border-radius: 4px 0px 0px 4px;
  color: white;
  -webkit-box-shadow: 1px 2px 5px rgba(0,0,0,.09);
  -moz-box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  box-shadow: 1px 2px 5px rgba(0,0,0,.09); 
  border: solid 0px #cbc9c9;
}

.gender {
  margin-left: 30px;
  margin-bottom: 30px;
}

.accounttype{
  margin-left: 8px;
  margin-top: 20px;
}

a.button {
  text-align: center;
  font-size: 14px;
  font-weight: 600;
  color: white;
  padding: 6px 25px 0px 20px;
  margin: 10px 8px 20px 0px;
  display: inline-block;
  text-decoration: none;
  width: 50px; height: 27px; 
  -webkit-border-radius: 5px; 
  -moz-border-radius: 5px; 
  border-radius: 5px; 
  background-color: #3a57af; 
  -webkit-box-shadow: 0 3px rgba(58,87,175,.75); 
  -moz-box-shadow: 0 3px rgba(58,87,175,.75); 
  box-shadow: 0 3px rgba(58,87,175,.75);
  transition: all 0.1s linear 0s; 
  top: 0px;
  position: relative;
}

a.button:hover {
  top: 3px;
  background-color:#2e458b;
  -webkit-box-shadow: none; 
  -moz-box-shadow: none; 
  box-shadow: none;
  
}
                        
</style>
 
<div class="testbox">
  <h1>Registration</h1>

  <form action="/">
  <hr>
  <label id="icon" for="name"><i class="icon-envelope "></i></label>
  <input type="text" name="name" id="name" placeholder="Email" required/>
  <label id="icon" for="name"><i class="icon-user"></i></label>
  <input type="text" name="name" id="name" placeholder="Name" required/>
  <label id="icon" for="name"><i class="icon-shield"></i></label>
  <input type="password" name="name" id="name" placeholder="Password" required/>
  <div class="gender">
    <label for="male" name="gender">Gender</label> </br>
    <input type="radio" value="None" id="male" name="gender" checked/>
    <label for="male" class="radio" chec>Male</label>
    <input type="radio" value="None" id="female" name="gender" />
    <label for="female" class="radio">Female</label>
   </div> 

   <p>  <input type="checkbox" /> I have read all the <a href="#">terms and condition</a>.</p>
   <a href="http://127.0.0.1:7000/Login/" class="button">Register</a>
   <p> Already have an Account ? <a href="#"> Register</a></p>
  </form>
</div>
                        
''')
