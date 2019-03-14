// GENERATE MAP

let map_element = L.map('map-reference').setView([52.368, 5.5], 9);

// Mapbox maps tile
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoia3dhbnN1cHAiLCJhIjoiY2p0NjZwZXplMDNoczQ0cWwzZ3IzNHJsdiJ9.zqrnapW2W_gpZrtLu5dSMQ'
}).addTo(map_element);

map_element.invalidateSize();

// // OSM original tiles
// L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
//         attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//     }).addTo(map);


// INTERACTION WITH ITEM
let item = document.getElementsByClassName('item');
let marker = new L.marker([52.368, 5.5]);



// $(item).hover(function() {
// 	$(this).toggleClass('marker');
// 	map.addLayer(marker);
// 	$('#map-caption').text($(this).text());
// }, function() {
// 	$(this).toggleClass('marker');
// 	map.removeLayer(marker);
// 	$('#map-caption').text('Hover over item');
// });
