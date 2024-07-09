$(document).ready(function() {
    $('#add-note-btn').click(function() {
        if ($('.additional-notes div').length >= 10) {
            alert('Has alcanzado el límite de notas Máximo (10).');
            return;
        }
    

        var newNoteDiv = '<div class="mb-3"><label for="nota' + 
        (parseInt($('.additional-notes div').length) + 1) + 
        '" class="form-label">Nota ' + 
        (parseInt($('.additional-notes div').length) + 1) + 
        ':</label><input type="number" class="form-control" id="nota'+ 
        (parseInt($('.additional-notes div').length) + 1) + 
        '" min="0" max="100" name="note-additional" required></div>';
          
        $('.additional-notes').append(newNoteDiv);
    });

    $('#delete-note').click(function(){
        if ($('.additional-notes div').length <= 2) {
            alert('No puedes eliminar todas las notas.');
            return;
        }
            $('.additional-notes div:last-child').remove();
        });
    $('#calculator-form').submit(function(event){
        event.preventDefault();//evita que el formulario se envie
    });
    $('#calculator-form').validate({
        rules:{
            nota1:{
                required:true,
                min:20,
                max:70,
                number:true
            },
            nota2:{
                required:true,
                min:20,
                max:70,
                number:true
            },
            'note-additional':{
                required:true,
                min:20,
                max:70,
                number:true
            },
            nota_examen:{
                required:true,
                min:20,
                max:70,
                number:true
            },
        },
        messages: {
            nota1 :{
            required:"El campo no debe estar vacio",
            min:"La nota debe ser mayor a 20",
            max:"La nota debe ser menor a 70",
            number:"Debe ingresar valores numericos entre 20-70"
            },
            nota2 :{
            required:"El campo no debe estar vacio",
            min:"La nota debe ser mayor a 20",
            max:"La nota debe ser menor a 70",
            number:"Debe ingresar valores numericos entre 20-70"
            },
            'note-additional':{
                required:"El campo no debe estar vacio",
                min:"La nota debe ser mayor a 20",
                max:"La nota debe ser menor a 70",
                number:"Debe ingresar valores numericos entre 20-70"
            },
            nota_examen:{
                required:"El campo no debe estar vacio",
                min:"La nota debe ser mayor a 20",
                max:"La nota debe ser menor a 70",
                number:"Debe ingresar valores numericos entre 20-70"
            }
        }
    });
});