function mascara(i){
   
    var v = i.value;
    
    if(isNaN(v[v.length-1])){ // impede entrar outro caractere que não seja número
       i.value = v.substring(0, v.length-1);
       return;
    }
    
    i.setAttribute("maxlength", "14");
    if (v.length == 3 || v.length == 7) i.value += ".";
    if (v.length == 11) i.value += "-";
 
 }
 
 

function verificapw(){

   var password = document.getElementById('password').value;
   var feed = document.getElementsByClassName('feed');
   var btnCadastrar = document.getElementById('cadastrar');
       
   var maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
   var numeros = "0123456789";

   var letras  = [];
   var num     = [];

   function mudacor_feed(f, c){ /*f - feed, c - cor*/
      var cor = ["#2fdc2f","#ff383b"]
     feed[f].style.color =  cor[c]
   }
   
   if (password.length == 0){
      mudacor_feed(1,1);
      mudacor_feed(2,1);
      mudacor_feed(3,1);
      
   }
  

   for (i=0;i<password.length;i++){
      
      letras.push(maiusculas.indexOf(password.charAt(i)))
      num.push(numeros.indexOf(password.charAt(i)))
    
      var maxLetras = Math.max.apply(null, letras);
      var maxNum = Math.max.apply(null, num);
     
      if (password.length >= 8){
         mudacor_feed(1,0);  
      } else {
         mudacor_feed(1,1);
      }

      if (maxLetras >=0){
         mudacor_feed(2,0);
      } else{
         mudacor_feed(2,1);
      }

      if (maxNum >=0){
         mudacor_feed(3,0); 
      } else{
         mudacor_feed(3,1); 
      }

      


      if (maxLetras>=0 & maxNum >= 0 & password.length >=8){
         btnCadastrar.disabled = false;
      }else{
         btnCadastrar.disabled = true; 
      }

      /*======verifca se tem letras =======
      if (maiusculas.indexOf(password.charAt(i)) != '-1'){
         feed[1].style.color = "#2fdc2f";  
         letras.push(maiusculas.indexOf(password.charAt(i)))  
      } else {
         letras.push(maiusculas.indexOf(password.charAt(i)))
         feed[1].style.color = "#ff383b";
      }*/
  
   }


}

function mask(o, f) {
   setTimeout(function() {
     var v = mphone(o.value);
     if (v != o.value) {
       o.value = v;
     }
   }, 1);
 }
 
 function mphone(v) {
   var r = v.replace(/\D/g, "");
   r = r.replace(/^0/, "");
   if (r.length > 10) {
     r = r.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
   } else if (r.length > 5) {
     r = r.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
   } else if (r.length > 2) {
     r = r.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
   } else {
     r = r.replace(/^(\d*)/, "($1");
   }
   return r;
 }

 $(document).ready(function(){
   $("#id_cep").mask("00000-00");
  
 })

 