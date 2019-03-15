
// GENERATE MAP

var map_element = L.map('map-reference').setView([52.368, 5.5], 9);

// Mapbox maps tile
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: '',
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
var marker = L.marker([52.368, 5.5]).addTo(map_element);

//var popup = L.popup();
//
function onMapClick(e) {
    var newMarker = new L.marker(e.latlng).addTo(map_element);
}

map_element.on('click', onMapClick);


// $(item).hover(function() {
// 	$(this).toggleClass('marker');
// 	map.addLayer(marker);
// 	$('#map-caption').text($(this).text());
// }, function() {
// 	$(this).toggleClass('marker');
// 	map.removeLayer(marker);
// 	$('#map-caption').text('Hover over item');
// });
