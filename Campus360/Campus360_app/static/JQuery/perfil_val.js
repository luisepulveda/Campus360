$(document).ready(function(){
    var users = JSON.parse(localStorage.getItem('users'));
    if(users && users.length > 0) {
        var latestUser = users[users.length - 1];
        $('#profile-username').text(latestUser.username);
        $('#profile-email').text('Correo Electrónico: ' + latestUser.email);
        // Aquí puedes agregar más campos del perfil si es necesario
    }
});