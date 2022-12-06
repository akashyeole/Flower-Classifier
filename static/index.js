function getImg(evt){
    const predict_button = document.getElementById("predict-btn");
    const evnt = document.getElementById("uploadBox");
    if(evnt.value == "") {
        predict_button.setAttribute("disabled", "");
    }else{
        // console.log(evnt.target.files[0]);
        // print(evnt)
        var fr = new FileReader();
        fr.onload = function(){
            // console.log("HI");
            url = fr.result;
            document.getElementById("myimg").src = url;
            document.getElementById("myimg").style.display = "inline-block";
            document.getElementById("filelab").style.display = "none";
            document.getElementById("uploadBox").style.display = "none";
            // bgele.setAttribute("background-image", url);
            // window.location.href = url;
        }
        fr.readAsDataURL(evnt.files[0]);
        predict_button.removeAttribute("disabled");
    }
}

function submitting(){
    const predict_button = document.getElementById("predict-btn");
    const choose_another_button = document.getElementById("choose-another");
    predict_button.setAttribute("disabled", "");
    choose_another_button.setAttribute("disabled", "");
}