function searchProperty() {

let input = document.getElementById("search").value.toLowerCase();

let property = document.querySelector(".property-card");

let title = document.querySelector(".property-title").innerText.toLowerCase();

if(title.includes(input)) {

property.style.display = "block";

}

else {

property.style.display = "none";

}

}