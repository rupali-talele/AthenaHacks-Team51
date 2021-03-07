window.onload = function()
{
    var timer = document.querySelector(".timer");
    timer.innerHTML = "1 mins 0 secs";
    var st = document.getElementsByClassName("start")
    console.log("DOM LOADED")
        // declare variables for star icons
    const smile = document.querySelectorAll(".smile");
    // stars list
    var smilesList = document.querySelectorAll(".smiles li");
    // // close icon in modal
    // var closeicon = document.querySelector(".close");
    // declare modal
    var modal = document.getElementById("popup1") 
var second = 0, minute = 1; hour = 0;
var timer = document.querySelector(".timer");
var play = document.getElementById("play-again")
 
}
var interval;   

function startGame(){

    console.log("startgame")
    // reset rating
    // for (var i= 0; i < smile.length; i++){
    //     smile[i].style.visibility = "visible";
    // }
    //reset timer
    second = 0;
    minute = 1;
    var st = document.getElementById("start")
    st.style.display = "block"
    clearInterval(interval);
    startTimer();
}

function startTimer(){
    var timer = document.querySelector(".timer");
    interval = setInterval(function(){
        timer.innerHTML = minute+" mins "+second+" secs";
        if(second == 0){
            minute--;
            second=3;
        }
        second--;
        if(second == 0 && minute == 0){
            congratulations()
        }
    },1000);
}


// @description congratulations when all cards match, show modal and moves, time and rating
function congratulations(){
    clearInterval(interval);

    // show congratulations modal
    var modal = document.getElementById("modal")
    modal.style.display = "block"
    // declare star rating variable
    var smileRating = document.querySelector(".smiles").innerHTML;

    //showing move, rating, time on modal
    // document.getElementById("smileRating").innerHTML = smileRating;

    //closeicon on modal
    // closeModal();
    

    

}

function closemodal()
{
    var modal = document.getElementById("modal")
    modal.style.display="none"
}

function gohome()
{
    window.location.replace("http://127.0.0.1:5000/static/welcome.html")
}

// // @description close icon on modal
// function closeModal(){
//     closeicon.addEventListener("click", function(e){
//         modal.classList.remove("show");
//         startGame();
//     });
// }


// @desciption for user to play Again
function playAgain(){
    // modal.classList.remove("show");
    closemodal();
    startGame();
}


// loop to add event listeners to each card
// for (var i = 0; i < cards.length; i++){
//     card = cards[i];
//     card.addEventListener("click", displayCard);
//     card.addEventListener("click", cardOpen);
//     card.addEventListener("click",congratulations);
// };
