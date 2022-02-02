// this of checkbox method
var inputPass = document.getElementById('pass'),
inputChk  = document.getElementById('chk'),
label = document.getElementById('showhide');


inputChk.onclick = function () {

if(inputChk.checked) {

     inputPass.setAttribute('type', 'text');
     label.textContent = 'Hide Password';
 } else {

     inputPass.setAttribute('type', 'password');
     label.textContent = 'Show Password';
 }

}
