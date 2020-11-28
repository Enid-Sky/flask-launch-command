'use strict';


// countdown

function createCountdown() {
    const promise = fetch('/data');

    promise
        .then(function (response) {
            const processingPromise = response.json();
            return processingPromise;
        })
        .then (function (data) {
            console.log('GET response:');
            console.log(data.date);
            console.log(data.name);
            console.log(data.second_name)
            console.log(data.second_launch)

            // Output the rocket name in an element
            document.getElementById("rocketName").innerHTML = `${data.name}`;
        
            // console.log('window')
            // console.log(window.launch.time);

            // Update the count down every 1 second
            const currentCountdown = setInterval(function() {
            
            const countDownDate = new Date(data.date).getTime();

            // Get today's date and time
            const now = new Date().getTime();
                
            // Time difference between now and the countdown time
            let timeRemaining = countDownDate - now;
            
            // Time calculations for days, hours, minutes and seconds
            const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
                
            // Output the result in an element with id="countdown
            document.getElementById("countdown").innerHTML = `${days} : ${hours} : ${minutes} : ${seconds}`;
                
            // If the count down is over, display 0,0,0,0 and name of next launch
                if (timeRemaining < 0) {
                    document.getElementById("rocketName").innerHTML = `${data.second_name}`;
                    clearInterval(currentCountdown);
                    document.getElementById("countdown").innerHTML = "0: 0: 0: 0";

                }
            }, 1000);
        });
        // return data.date;
}

// FUNCTION CALLS
createCountdown()









