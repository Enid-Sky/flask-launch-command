'use strict';

$("#follow_input").on('click', () => {
    
    // change button text on click
    if ($("#follow_input").text() === "Follow") {
        $("#follow_input").text("Unfollow");
    // change button text back on click
    } else {
        $("#follow_input").text("Follow");
    }
});
