'use strict';

function getData() {
    fetch('/data')
        .then(function (response) {
            return response.json();
        })
        .then (function (text) {
            console.log('GET response:');
            console.log(text.date);
        });
        test = text.date
        document.getElementById("date").innerHTML = `${test}`
        return test;     
};


function countdown(data) {
    const countDownDate = new Date(data).getTime();
    console.log('window')
    console.log(window.launch.time);

    // Update the count down every 1 second
    const currentCountdown = setInterval(function() {

    // Get today's date and time
    const now = new Date().getTime();
        
    // Time difference between now and the countdown time
    const timeRemaining = countDownDate - now;
        
    // Time calculations for days, hours, minutes and seconds
    const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
        
    // Output the result in an element with id="countdown
    document.getElementById("countdown").innerHTML = `${days} : ${hours} : ${minutes} : ${seconds}`;
        
    // If the count down is over, 
        if (timeRemaining < 0) {
            clearInterval(currentCountdown);
            document.getElementById("countdown").innerHTML = "ENDED";
        }
    }, 1000);

}





$("#follow_input").on('click', () => {
    
    // change button text on click
    if ($("#follow_input").text() === "Follow") {
        $("#follow_input").text("Unfollow");
    // change button text back on click
    } else {
        $("#follow_input").text("Follow");
    }
});


// FUNCTION CALLS
countdown()
getData()
