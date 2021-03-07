var domain = "http://127.0.0.1:5000"

window.onload = function()
{    
    console.log("DOM LOADED");    
    console.log("addaccount.js"); 
    var uid = document.getElementById("uid")
    var age = document.getElementById("age")
    var pwd = document.getElementById("pwd")
    // console.log(uid)
    // console.log(age)
    // console.log(pwd)    
}

function addaccountinfo()
{

    console.log("addaccountinfo called")
    var n = uid.value
    var p = pwd.value
    var a = age.value
    params = "username="+n+"&pwd="+p+"&age="+a
    console.log(n)
    console.log(p)
    console.log(a)

    var xhttp = new XMLHttpRequest(); 
    var url = domain+"/add?"+params      
    console.log(url)
    xhttp.open("POST", url , true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.responseType = 'json';
    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200) {  
            console.log(this.response)
            if(this.response["status"]=="success")
            {
                console.log(this.response)
                window.location.replace("http://127.0.0.1:5000/static/welcome.html");
            }  
        }
    }  
    console.log(params)
    xhttp.send();
}