// switch on

let delay_before_first_message = 5000;
let delay_before_second_message = 8000;
let delay_before_hide = 14000; 

function unhide_box() { 
    document.getElementById("my_alert_box").setAttribute("id", "unhide_box");
};

function switch_time_on() {
    time_on = window.setTimeout(unhide_box, delay_before_first_message);
};

document.addEventListener('DOMContentLoaded', switch_time_on);



// middle message

let middle_message = "Нажми на слово, чтобы перейти на неслучайное стихотворение"; 

function insert_middle_message() { 
    document.getElementById("unhide_box").innerHTML = middle_message;
};

function switch_middle_time() {
    time_middle = window.setTimeout(insert_middle_message, delay_before_second_message);
};
    
document.addEventListener('DOMContentLoaded', switch_middle_time)

    
    

// switch off

function hide_box() {
   document.getElementById("unhide_box").setAttribute("id", "my_alert_box");
}

function switch_time_off(){
    time_off = window.setTimeout(hide_box, delay_before_hide);
}

document.addEventListener('DOMContentLoaded', switch_time_off);


