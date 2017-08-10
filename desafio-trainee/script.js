document.getElementById("login-form").onsubmit = function validaCampo(){
	var email = document.getElementById('email');
	var txt   = document.getElementById('email').value;
	var n     = txt.length;
	var senha = document.getElementById('senha');
	var snh = document.getElementById('senha').value;
	var s = snh.length;
	

if(n == 0 || s < 6){
    alert("Confira seus dados e tente novamente!");
    return false;
    
    email.focus();
}

document.getElementById("cadastrar-popup").style.display = "inline";

return false;

}
