$(document).ready(function () {
    var cart = JSON.parse(localStorage.getItem("cart")) || [];
    var cartOutput = $("#cart-output");

    function displayCart() {
        cartOutput.empty();
        if (cart.length === 0) {
            cartOutput.append("<p class='text-center'>El carrito está vacío</p>");
        } else {
            cart.forEach(function (item, index) {
                var htmlContent = `
                <div class="col-lg-4 col-md-6 col-sm-12 mb-4">
                    <div class="card" style="width: 18rem;">
                        <img src="${item.img}" class="card-img-top" alt="${item.title}">
                        <div class="card-body">
                            <h5 class="card-title">${item.title}</h5>
                            <p class="card-text">Autor: ${item.author}</p>
                            <p class="card-text c v">Editorial: ${item.publisher}</p>
                            <p class="card-text">Precio: $${item.price}</p>
                            <input type="number" class="form-control mb-2 quantity" data-index="${index}" value="${item.quantity}">
                            <button class="btn btn-danger remove-from-cart" data-index="${index}">Eliminar</button>
                        </div>
                    </div>
                </div>`;
                cartOutput.append(htmlContent);
            });
            $(".remove-from-cart").click(removeFromCart);
            $(".quantity").change(updateQuantity);
        }
    }

    function addToCart(item) {
        var exists = cart.find(cartItem => cartItem.title === item.title);
        if (exists) {
            exists.quantity += 1;
        } else {
            cart.push({ ...item, quantity: 1 });
        }
        localStorage.setItem("cart", JSON.stringify(cart));
        displayCart();
        showAlert('Libro agregado al carrito');
    }

    function removeFromCart(event) {
        var index = $(this).data("index");
        cart.splice(index, 1);
        localStorage.setItem("cart", JSON.stringify(cart));
        displayCart();
        showAlert('Libro eliminado del carrito');
    }

    function updateQuantity(event) {
        var index = $(this).data("index");
        var quantity = $(this).val();
        cart[index].quantity = parseInt(quantity);
        localStorage.setItem("cart", JSON.stringify(cart));
        displayCart();
    }

    function showAlert(message) {
        var alert = $('<div class="alert alert-success alert-dismissible fade show" role="alert">' +
                      message +
                      '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                      '<span aria-hidden="true">&times;</span>' +
                      '</button>' +
                      '</div>');
        $('body').append(alert);
        setTimeout(function() {
            alert.alert('close');
        }, 3000);
    }

    $("#checkout").click(function () {
        alert("Procesando el pago...");
        // Aquí podrías redirigir a una pasarela de pago o realizar alguna otra acción.
    });

    displayCart();
});
