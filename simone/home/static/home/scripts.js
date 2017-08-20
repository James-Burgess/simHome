buttonList = document.getElementById("buttons").getElementsByTagName("a");

var xhr = new XMLHttpRequest();
var vbg = new XMLHttpRequest();


for (i = 0; i < buttonList.length; i++){
	buttonList[i].addEventListener('click', change);
	console.log(buttonList[i].id)
}

function change(e){
	var num = e.target.id;
	console.log(event.target.id)
	if(e.target.classList.contains('off')){
		e.target.classList.remove('off');
		e.target.classList.add('on');
		xhr.open('GET', "/submit/"+num, true);
		xhr.send();

	}
		else{
		e.target.classList.remove('on');
		e.target.classList.add('off');
		vbg.open('GET', "/submit/"+num, true);
		vbg.send();
	}
}