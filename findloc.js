async function getLocation() {
    if (navigator.geolocation) {
        await navigator.geolocation.getCurrentPosition(showPosition, showError)
        initMap(latitude, longitude);
    } 
    else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

async function showPosition(position) {
    latitude = position.coords.latitude
    longitude = position.coords.longitude
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude; 
}

async function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation. cock cock cock"
            break;

        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable."
            break;

        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out."
            break;

        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred."
            break;
    }
}