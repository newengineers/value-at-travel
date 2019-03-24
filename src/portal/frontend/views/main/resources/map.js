
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

// Locate
// variable to contain current location
var currentLocation = [0, 0]
// on locate, zoom and keep watch
map_element.locate({setView: true,
			maxZoom: 16,
			watch: true
});

map_element.on('locationfound', function(e) {
	var radius = e.accuracy / 10;
	console.log(e.latlng)
	L.marker(e.latlng).addTo(map_element)
		.bindPopup("You are within " + radius + " meters from this point").openPopup();
	L.circle(e.latlng, radius).addTo(map_element);
});


// // GEOLOCATION ALTERNATIVE
//navigator.geolocation.getCurrentPosition(function(location) {
//  var latlng = new L.LatLng(location.coords.latitude, location.coords.longitude);
//
//  var mymap = L.map('mapid').setView(latlng, 13)
//  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
//    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://mapbox.com">Mapbox</a>',
//    maxZoom: 18,
//    id: 'mapbox.streets',
//    accessToken: 'pk.eyJ1IjoiYmJyb29rMTU0IiwiYSI6ImNpcXN3dnJrdDAwMGNmd250bjhvZXpnbWsifQ.Nf9Zkfchos577IanoKMoYQ'
//  }).addTo(mymap);
//
//  var marker = L.marker(latlng).addTo(mymap);
//});


// INTERACTION WITH MAP

var marker = {};
// map_element.on('click', onMapClick);
map_element.on('click', function(e) {
	// location = e.latlng

	if (marker != undefined) {
		map_element.removeLayer(marker);
	}

	// add marker to clicked location
	marker = L.marker(e.latlng).addTo(map_element);
});