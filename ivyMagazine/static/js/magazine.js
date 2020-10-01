const navLeft = document.getElementsByClassName("left");
const navRight = document.getElementsByClassName("right");

const images = document.getElementsByClassName("images");
const colors = document.getElementsByClassName("colored-backgrounds");

function viewMagazine(){
    console.log("viewMagazine");
}

let index = 0;

function right() {
    console.log("right is clicked!")
  transform((index = index < 3 ? ++index : 0));
}

function left() {
  transform((index = index > 0 ? --index : 3));
}

function transform(index) {
    images.style.transform = `translateX(-${index * 100}%)`;
    colors.style.transform = `translateX(-${index * 100}%)`;
}

navLeft.addEventListener("click", left);
navRight.addEventListener("click", right);


