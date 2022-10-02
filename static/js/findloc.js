function retrieveFriends(request) {
    // with data from database, loads all users in div
    var data = request.response
    document.getElementById("friends").setInnerText(data)
}