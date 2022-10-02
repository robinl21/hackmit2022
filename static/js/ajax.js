(function (global) {
    var ajaxutils = {}; 

    function getRequestObject () {
        return (new XMLHttpRequest());
    }

    function handleResponse (request, responseHandler) {
        if ((request.readyState == 4) && (request.status == 200)) {
            responseHandler(request);
        }
        
        else {
            alert("Bad request!");
        }
    }

    ajaxutils.sendGetRequest = function (requestUrl, responseHandler, responseType) {
        var request = getRequestObject();
        request.onload = function () {
            handleResponse(request, responseHandler);
        }
        request.open("GET", requestUrl, true);
        request.responseType = responseType;
        request.send(null); 
    }

    ajaxutils.sendPostRequest = function(requestUrl, params) {
        var request = getRequestObject();
        request.onload = function () {
            if ((request.readyState == 4) && (request.status == 200)) {
                alert("Information Sent")
            }
            
            else {
                alert("BAD REQUEST!")
            }
        }
        request.open('POST', requestUrl, true);
        request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        request.send(params);
    }

    global.$ajaxutils = ajaxutils
})(window);
