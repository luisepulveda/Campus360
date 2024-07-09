$(document).ready(function(){
    $('#Contenido').validate({
        rules: {
            username: {
                required: true,
                minlength: 5
            },
            email: {
                required: true,
                email: true,
                minlength: 1
            },
            password: {
                required: true,
                minlength: 8
            }
        },
        messages: {
            username: {
                required: "Por favor, introduzca el nombre",
                minlength: "Debe tener un mínimo de 5 caracteres"
            },
            email: {
                required: "Por favor, introduzca el correo",
                minlength: "Debe ser un correo válido",
                email: "Debe ser un correo con formato válido"
            },
            password: {
                required: "Por favor, introduzca la contraseña",
                minlength: "Debe tener un mínimo de 8 caracteres"
            }
        },
        submitHandler: function(form) {
            saveUser();
            form.reset();
            return false;
        }
    });

    function saveUser(){
        var username = $('#username').val();
        var email = $('#email').val();
        var password = $('#password').val();
        var user = {username, email, password};
        saveUserToStorage(user);
    }

    function saveUserToStorage(user){
        var users = localStorage.getItem('users') ? JSON.parse(localStorage.getItem('users')) : [];
        users.push(user);
        localStorage.setItem('users', JSON.stringify(users));
        alert('Usuario creado con éxito');
        console.log(localStorage.getItem('users'));
    }
});
