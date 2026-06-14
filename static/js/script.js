// Dark Mode

const themeBtn =
document.getElementById("themeBtn");

if(themeBtn){

themeBtn.addEventListener("click",()=>{

document.body.classList.toggle(
"dark-mode"
);

localStorage.setItem(
"theme",
document.body.classList.contains(
"dark-mode"
)
);

});

if(localStorage.getItem("theme")
==="true"){

document.body.classList.add(
"dark-mode"
);

}

}


// Character Counter

const textarea =
document.getElementById(
"postContent"
);

const count =
document.getElementById(
"count"
);

if(textarea){

textarea.addEventListener(
"input",
()=>{

count.innerText =
300 -
textarea.value.length;

});

}


// Image Preview

const imageInput =
document.getElementById(
"imageInput"
);

const preview =
document.getElementById(
"preview"
);

if(imageInput){

imageInput.addEventListener(
"change",
function(){

let file =
this.files[0];

if(file){

preview.src =
URL.createObjectURL(
file
);

preview.style.display =
"block";

}

});

}


// Scroll Top Button

const topBtn =
document.getElementById(
"topBtn"
);

window.onscroll =
function(){

if(
document.documentElement
.scrollTop > 200
){

topBtn.style.display =
"block";

}else{

topBtn.style.display =
"none";

}

};

if(topBtn){

topBtn.onclick =
function(){

window.scrollTo({

top:0,
behavior:"smooth"

});

};

}


// Delete Confirmation

function confirmDelete(){

return confirm(
"Delete this post?"
);

}