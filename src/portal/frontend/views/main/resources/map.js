
// GENERATE MAP

var map_element = L.map('map-reference').setView([52.368, 5.5], 9);

// Mapbox maps tile
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: '',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoia3dhbnN1cHAiLCJhIjoiY2p0NjZwZXplMDNoczQ0cWwzZ3IzNHJsdiJ9.zqrnapW2W_gpZrtLu5dSMQ'
}).addTo(map_element);
L.Control.geocoder().addTo(map_element);

map_element.invalidateSize();

// // OSM original tiles
// L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
//         attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
//     }).addTo(map);

// Locate
// initiate list variable to contain current location latitude and longitude
var currentLocation = [0, 0]
// on locate, zoom and keep watch
map_element.locate({setView: true,
			maxZoom: 16,
			watch: true
});

map_element.on('locationfound', function(e) {
	var radius = e.accuracy / 10;
	currentLocation = [e.latlng.lat, e.latlng.lng]
	console.log("currentLocation: ", currentLocation)
    control.spliceWaypoints(0, 1, e.latlng);
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


control = L.Routing.control({
    waypoints: [
        L.latLng(),
        L.latLng()
    ],
    router: L.Routing.mapbox('pk.eyJ1Ijoia3dhbnN1cHAiLCJhIjoiY2p0NjZwZXplMDNoczQ0cWwzZ3IzNHJsdiJ9.zqrnapW2W_gpZrtLu5dSMQ',{
    	//possible profiles: mapbox/driving-traffic, mapbox/driving, mapbox/walking, mapbox/cycling
    	profile: 'mapbox/driving'
		}),
	reverseWaypoints: true,
    showAlternatives: true,
    geocoder: L.Control.Geocoder.nominatim(),
	//router: L.Routing.osrmv1("profile"),
    waypointNameFallback: function(latLng) {
        function zeroPad(n) {
            n = Math.round(n);
            return n < 10 ? '0' + n : n;
        }
        function sexagesimal(p, pos, neg) {
            var n = Math.abs(p),
                degs = Math.floor(n),
                mins = (n - degs) * 60,
                secs = (mins - Math.floor(mins)) * 60,
                frac = Math.round((secs - Math.floor(secs)) * 100);
            return (n >= 0 ? pos : neg) + degs + '°' +
                zeroPad(mins) + '\'' +
                zeroPad(secs) + '.' + zeroPad(frac) + '"';
        }

        return sexagesimal(latLng.lat, 'N', 'S') + ' ' + sexagesimal(latLng.lng, 'E', 'W');
    },
    altLineOptions: {
        styles: [
            {color: 'blue', opacity: 1, weight: 2}
        ]
    },
})
	//.on('routeselected', function(e) {
    //var route = e.route;
    //alert('Showing route between waypoints:\n' + JSON.stringify(route.inputWaypoints, null, 2));
//})
	.addTo(map_element);

L.Routing.errorControl(control).addTo(map_element);

// initiate list variable to store clicked location latitude and longitude
//var clickedLocation = [0, 0]
var marker = {};
function createButton(label, container) {
    var btn = L.DomUtil.create('button', '', container);
    btn.setAttribute('type', 'button');
    btn.innerHTML = label;
    return btn;
}




map_element.on('click', function(e) {
    var container = L.DomUtil.create('div'),
        startBtn = createButton('Start from this location', container),
        destBtn = createButton('Go to this location', container);

    L.popup()
        .setContent(container)
        .setLatLng(e.latlng)
        .openOn(map_element);

    L.DomEvent.on(startBtn, 'click', function() {
        control.spliceWaypoints(0, 1, e.latlng);
        map_element.closePopup();
    });
    L.DomEvent.on(destBtn, 'click', function() {
        control.spliceWaypoints(control.getWaypoints().length - 1, 1, e.latlng);
        map_element.closePopup();
    });
});

//var helloPopup = L.popup().setContent('Hello World!');

L.easyButton('<img src="http://cdn.onlinewebfonts.com/svg/img_427005.png" style="width:15px">', function(btn, map){
		//helloPopup.setLatLng(map.getCenter()).openOn(map);
    control.getRouter().options.profile = "mapbox/walking";
    control.route();
}).addTo( map_element );

/*
var clickedLocation = [0, 0]
var marker = {};
// map_element.on('click', onMapClick);
map_element.on('click', function(e) {
    clickedLocation = [e.latlng.lat, e.latlng.lng]
    console.log("clickedLocation: ", clickedLocation)

    if (marker != undefined) {
        map_element.removeLayer(marker);
    }

    // add marker to clicked location
    marker = L.marker(e.latlng).addTo(map_element);
});
*/