/* Author: Stephen Visser

*/

onClose = function(){
  document.getElementById('message').innerHTML = 'CLOSED';
};
onError = function(){
  document.getElementById('message').innerHTML = 'ERROR';
};
onMessage = function(message){
  document.getElementById('message').innerHTML = message;
};
onOpened = function(){
  document.getElementById('message').innerHTML = 'OPENED';
};
