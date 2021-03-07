

// declare variables for star icons
const smile = document.querySelectorAll(".smile");

 // stars list
 let smilesList = document.querySelectorAll(".smiles li");

 // close icon in modal
 let closeicon = document.querySelector(".close");

 // declare modal
 let modal = document.getElementById("popup1")

document.body.onload = startGame();


// @description function to start a new play
function startGame(){

    // reset rating
    for (var i= 0; i < smile.length; i++){
        smile[i].style.visibility = "visible";
    }
    //reset timer
    second = 0;
    minute = 1;
    var timer = document.querySelector(".timer");
    timer.innerHTML = "1 mins 0 secs";
    clearInterval(interval);
    startTimer();
}

// @description game timer
var second = 0, minute = 1; hour = 0;
var timer = document.querySelector(".timer");
var interval;
function startTimer(){
    var timer = document.querySelector(".timer");
    interval = setInterval(function(){
        timer.innerHTML = minute+" mins "+second+" secs";
        if(second == 0){
            minute--;
            second=60;
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
    let modal = document.getElementById("popup1")
    modal.classList.add("show");

    // declare star rating variable
    var smileRating = document.querySelector(".smiles").innerHTML;

    //showing move, rating, time on modal
    document.getElementById("smileRating").innerHTML = smileRating;

    //closeicon on modal
    closeModal();

}


// @description close icon on modal
function closeModal(){
    closeicon.addEventListener("click", function(e){
        modal.classList.remove("show");
        startGame();
    });
}


// @desciption for user to play Again
function playAgain(){
    modal.classList.remove("show");
    startGame();
}


// loop to add event listeners to each card
for (var i = 0; i < cards.length; i++){
    card = cards[i];
    card.addEventListener("click", displayCard);
    card.addEventListener("click", cardOpen);
    card.addEventListener("click",congratulations);
};
