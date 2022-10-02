function retrieveFriends(request) {
    // with data from database, loads all users in div
    friends = data
    var data = request.response
    console.log(data)
    var friendsBlock = document.getElementById("friends")
    friendsBlock.innerText=data
}