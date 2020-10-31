

const images = document.getElementsByClassName("images");
const colors = document.getElementsByClassName("colored-backgrounds");

const magBox = document.querySelector('.content');
const slides = document.getElementsByClassName('magazine');

const imageSlides = document.getElementsByClassName("images");

const navLeft = document.getElementsByClassName("left");
const navRight = document.getElementsByClassName("right");
var i = 0;
var j = 0;

function viewMagazine(pdfURL){
    console.log("viewMagazine");
}

function right() {
    slides[i].classList.remove('active');
    
    i = (i+1)% slides.length;
    slides[i].classList.add('active');
    
  //transform((index = index < 3 ? ++index : 0));
}

function left() {
  
  slides[i].classList.remove('active');
  i = (i-1 + slides.length)% slides.length;
  slides[i].classList.add('active');
  
}
function rightImg() {
  imageSlides[j].classList.remove('active');
  j = (j+1)% imageSlides.length;
  imageSlides[j].classList.add('active');

}

function leftImg() {
  imageSlides[j].classList.remove('active');
  j = (j-1 + imageSlides.length)% imageSlides.length;
  imageSlides[j].classList.add('active');
}

function transform(index) {
    images.style.transform = `translateX(-${index * 100}%)`;
    colors.style.transform = `translateX(-${index * 100}%)`;
}

navLeft.addEventListener("click", left);
navRight.addEventListener("click", right);
navLeft.addEventListener("click", leftImg);
navRight.addEventListener("click", rightImg);

