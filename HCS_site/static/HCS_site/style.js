menu.onclick = function myFunction(){
	var x = document.getElementById('myTopnav');

	if (x.className === "header-navigation"){
		x.className += "-responsive";
	} else{
		x.className = "header-navigation";
	}
}
