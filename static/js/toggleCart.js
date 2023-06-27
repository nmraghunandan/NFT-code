var button = document.getElementById('toggleCartButton' + box_id);

function toggleCart(box_id) {
    var button = document.getElementById(box_id).querySelector('.button');
    if (button.innerText === "Add to Cart") {
        cart.push(box_id);
        button.innerText = "Remove from Cart";
        button.style.backgroundColor = "red";
    } else {
        cart.splice(cart.indexOf(box_id), 1);
        button.innerText = "Add to Cart";
        button.style.backgroundColor = "";
    }
    updateCartInput();
}

function updateCartInput() {
    var cartInput = document.getElementById('cart-input');
    cartInput.value = cart.join(',');
    var cartForm = document.getElementById('cart-form');
    if (cart.length > 0) {
        cartForm.style.display = 'block';
    } else {
        cartForm.style.display = 'none';
    }
}

function goToCart() {
    var selectedBoxIds = "";
    for (var i = 0; i < cart.length; i++) {
        selectedBoxIds += cart[i] + ", ";
    }
    selectedBoxIds = selectedBoxIds.slice(0, -2); // remove trailing comma and space
    alert("Selected box IDs: " + selectedBoxIds);
    document.getElementById('cart-form').submit();
}