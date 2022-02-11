let offset = 0; //смещение от левого края
const sliderline= document.querySelector('.slider-line')

document.querySelector('.slider-next').addEventListener('click', function(){
  offset = offset + 840;
  if (offset > 2520){
    offset = 0;
  }
  sliderline.style.left=-offset+'px'
});

document.querySelector('.slider-prev').addEventListener('click', function(){
  offset = offset - 840;
  if (offset < 0){
    offset = 2520;
  }
  sliderline.style.left=-offset+'px'
});
