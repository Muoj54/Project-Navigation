document.addEventListener('DOMContentLoaded', (event) => {
    mapboxgl.accessToken = 'pk.eyJ1IjoibXVvajU0IiwiYSI6ImNseGV0OXFsMjBnNGsyanMzOTMzM2lrYWkifQ.fIyWhoRzZOFBFnkVMW2jxA';

    try {
        const jsonData = document.getElementById('location-data').textContent.trim();
        console.log('Raw JSON Data:', jsonData);
        
        // Ensure jsonData is properly formatted JSON
        const cleanJsonData = jsonData.replace(/(\r\n|\n|\r)/gm, "").replace(/\'/g, "\"");
        console.log('Clean JSON Data:', cleanJsonData);

        // Parse JSON data
        const locationData = JSON.parse(cleanJsonData);
        console.log('Location Data:', locationData);
        console.log('Type of Location Data:', typeof locationData);

        // Verify the parsed object and the bus_stops array
        if (locationData && typeof locationData === 'object') {
            const busStops = locationData.bus_stops; // Array of bus stops with lat, lng, and name
            console.log('Bus Stops:', busStops);
            console.log('Type of Bus Stops:', typeof busStops);
            console.log('Is Bus Stops Array:', Array.isArray(busStops));

            // Check if busStops is defined and is an array with elements
            if (busStops && Array.isArray(busStops) && busStops.length > 0) {
                // Proceed with map initialization and geolocation
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        (position) => {
                            const userLat = position.coords.latitude;
                            const userLng = position.coords.longitude;

                            // Initialize the map at the user's location
                            var map = new mapboxgl.Map({
                                container: 'map',
                                style: 'mapbox://styles/mapbox/streets-v11',
                                center: [userLng, userLat],
                                zoom: 12
                            });

                            new mapboxgl.Marker().setLngLat([userLng, userLat]).setPopup(new mapboxgl.Popup().setHTML("Your Location")).addTo(map);

                            // Find the nearest bus stop to the user
                            let nearestBusStop = null;
                            let minDistance = Infinity;

                            busStops.forEach(stop => {
                                const distance = getDistance(locationData.start_lat, locationData.start_lng, stop.latitude, stop.longitude);
                                if (distance < minDistance) {
                                    nearestBusStop = stop;
                                    minDistance = distance;
                                }
                            });

                            if (nearestBusStop) {
                                new mapboxgl.Marker().setLngLat([nearestBusStop.longitude, nearestBusStop.latitude]).setPopup(new mapboxgl.Popup().setHTML(nearestBusStop.name)).addTo(map);

                                // Get directions from user location to nearest bus stop
                                const url = `https://api.mapbox.com/directions/v5/mapbox/driving/${userLng},${userLat};${nearestBusStop.longitude},${nearestBusStop.latitude}?geometries=geojson&access_token=${mapboxgl.accessToken}`;
                                fetch(url)
                                    .then(response => response.json())
                                    .then(data => {
                                        if (data.routes && data.routes[0]) {
                                            const route = data.routes[0].geometry;
                                            map.addSource('route', {
                                                'type': 'geojson',
                                                'data': {
                                                    'type': 'Feature',
                                                    'properties': {},
                                                    'geometry': route
                                                }
                                            });
                                            map.addLayer({
                                                'id': 'route',
                                                'type': 'line',
                                                'source': 'route',
                                                'layout': {
                                                    'line-join': 'round',
                                                    'line-cap': 'round'
                                                },
                                                'paint': {
                                                    'line-color': '#ff0000',
                                                    'line-width': 8
                                                }
                                            });
                                        } else {
                                            console.error('No route found');
                                            alert('No route found');
                                        }
                                    })
                                    .catch(error => {
                                        console.error('Error calculating route', error);
                                        alert('Error calculating route');
                                    });
                            } else {
                                console.error('No bus stop found');
                                alert('No bus stop found');
                            }
                        },
                        (error) => {
                            console.error('Error getting user location', error);
                            // Fallback if geolocation fails
                            initializeMapWithDefaultLocation();
                        }
                    );
                } else {
                    console.error('Geolocation not supported by this browser.');
                    // Fallback if geolocation is not supported
                    initializeMapWithDefaultLocation();
                }
            } else {
                console.error('No bus stops found or bus_stops is not an array.');
                alert('No bus stops found.');
            }
        } else {
            console.error('Parsed location data is not an object.');
            alert('Error with location data format.');
        }

        function initializeMapWithDefaultLocation() {
            const userLat = 0; // default latitude
            const userLng = 0; // default longitude

            var map = new mapboxgl.Map({
                container: 'map',
                style: 'mapbox://styles/mapbox/streets-v11',
                center: [userLng, userLat],
                zoom: 12
            });

            new mapboxgl.Marker().setLngLat([userLng, userLat]).addTo(map);
        }

        function getDistance(lat1, lon1, lat2, lon2) {
            const R = 6371e3; // metres
            const φ1 = lat1 * Math.PI/180; // φ, λ in radians
            const φ2 = lat2 * Math.PI/180;
            const Δφ = (lat2-lat1) * Math.PI/180;
            const Δλ = (lon2-lon1) * Math.PI/180;

            const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
                      Math.cos(φ1) * Math.cos(φ2) *
                      Math.sin(Δλ/2) * Math.sin(Δλ/2);
            const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

            const d = R * c; // in metres
            return d;
        }
    } catch (error) {
        console.error('Error parsing location data', error);
    }
});
