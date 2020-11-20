'use strict';


// Set the date we're counting down to
fetch('https://ll.thespacedevs.com/2.0.0/launch/upcoming/?limit=5/?format=json')
.then((res) => {
    let data = res.json();
    let results = data['results']
    console.log(results);
    return results;
})

.then((results) => {
    let nextLaunch = results['start_window'];
    

    const countDownDate = new Date(nextLaunch).getTime();
    // Update the count down every 1 second
    const x = setInterval(function() {

    // Get today's date and time
    const now = new Date().getTime();
        
    // Find the distance between now and the count down date
    const distance = countDownDate - now;
        
    // Time calculations for days, hours, minutes and seconds
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = days + "d : " + hours + "h "
    + minutes + "m " + seconds + "s ";
        
    // If the count down is over, write some text 
        if (distance < 0) {
            clearInterval(x);
            document.getElementById("demo").innerHTML = "ENDED";
        }
    }, 1000);

})



$("#follow_input").on('click', () => {
    
    // change button text on click
    if ($("#follow_input").text() === "Follow") {
        $("#follow_input").text("Unfollow");
    // change button text back on click
    } else {
        $("#follow_input").text("Follow");
    }
});
