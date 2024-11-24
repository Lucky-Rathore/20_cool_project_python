// 
var socket = io();

socket.on('connect', function() {
    console.log('Connected');
});

socket.on('message', function(msg) {
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(msg));
    document.getElementById("messages").appendChild(li);
});

function sendMessage() {
    var input = document.getElementById("input");
    if (input.value) {
        socket.send(input.value);
        input.value = '';
    }
}