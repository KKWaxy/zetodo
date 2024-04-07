const title = document.getElementById('title')
title.focus()

var tasklist = document.getElementById("taskList");
var tasklistHeight = tasklist.offsetHeight;
var taskListTop = tasklist.offsetTop;

if (tasklistHeight >=194) {
    tasklist.classList.add("scroll");
    window.scrollTo(0,320);
}

var input_priority = document.getElementById('id_duedate');
input_priority.classList.add("form-control");




