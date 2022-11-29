"use strict"

const my_element = document.getElementById("my_alert_box");
let my_interval = 200;
let plus_step = 0.025;
let minus_step = -plus_step; 
let initial_pause = 2000;
let time_to_run_push_message = 1/plus_step * my_interval;
const list_of_timeouts = [
    initial_pause,
    initial_pause + time_to_run_push_message,
    initial_pause + 2*time_to_run_push_message,
    initial_pause + 3*time_to_run_push_message,
];
let text_1 = "Обнови страницу, чтобы собрать стихотворение из случайных слов"; 
let text_2 = "Нажми на слово, чтобы перейти к неслучайному стихотворению"; 


function push_message(start, step, cond, text) {
    let i = start;
    function fade_in(step, cond, text) {
        i += step;
        i = Number((i).toFixed(3));
        console.log("push__", i);
        let transparancy_level = `rgba(143, 188, 143, ${i})`;
        my_element.innerHTML = text; 
        my_element.style.setProperty("color", transparancy_level);
        if (i == cond) {
            clearInterval(tick);
        };
    
    }

    const tick = setInterval(fade_in, my_interval, step, cond, text);
};


setTimeout("push_message(0, plus_step, 1, text_1)", list_of_timeouts[0]);
setTimeout("push_message(1, minus_step, 0, text_1)", list_of_timeouts[1]);
setTimeout("push_message(0, plus_step, 1, text_2)", list_of_timeouts[2]);
setTimeout("push_message(1, minus_step, 0, text_2)", list_of_timeouts[3]);
