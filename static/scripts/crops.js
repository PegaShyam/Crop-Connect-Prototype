var select = document.getElementById("selectCrop");
var options = new Array("apple", "banana", "blackgram", "chickpea", "coconut", "coffee", "cotton", "grapes", "jute", "kidneybeans", "lentil", "maize", "mango", "mothbeans", "mungbean", "muskmelon", "orange", "papaya", "pigeonpeas", "pomegranate", "rice", "watermelon");
for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
}
var select = document.getElementById("selectSeason");
var options = new Array('autumn', 'kharif', 'rabi',
'summer', 'whole year', 'winter');
for(var i = 0; i < options.length; i++) {
    var opt = options[i];
    var el = document.createElement("option");
    el.textContent = opt;
    el.value = opt;
    select.appendChild(el);
}
