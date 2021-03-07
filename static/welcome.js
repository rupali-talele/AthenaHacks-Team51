window.onload = function()
{
    
    var smiles = document.getElementById("smiles")
    smiles.innerHTML = window.localStorage.getItem("smiles");
    
}

function checkin()
{
    var checkin = document.getElementById("checkin")
    var checkout = document.getElementById("checkout")
    checkin.style.display = "none"
    checkout.style.display = "block"
    window.location.replace("http://localhost:5000/static/Check-in/check-in.html")
}

function checkout()
{
    var checkin = document.getElementById("checkin")
    var checkout = document.getElementById("checkout")
    checkin.style.display = "block"
    checkout.style.display = "none"
    window.location.replace("http://localhost:5000/static/check-out/check-out.html")
}