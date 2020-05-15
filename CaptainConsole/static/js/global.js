/**
 * Function makes an AJAX request which adds
 * a given quantity of the product to the users shopping cart.
 * @param {String} product_id ID of the given product
 * @param {String} product_name Name of the given product
 * @param {String} quantity Quantity of product to put in shopping cart
 */
function add_to_shopping_cart(product_id, product_name, quantity) {
    quantity = Number(quantity);
    if (quantity > 32767) {
        M.toast({ html: "Specified quantity is too high." });
        return false;
    }

    if (quantity > 0) {
        let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: "/cart/ajax/add_item/",
            method: "POST",
            data: {
                product_id: product_id,
                quantity: quantity,
                csrfmiddlewaretoken: csrftoken,
            },
            success: function (result) {
                if (result.message === 'LOGIN NEEDED') {
                    M.toast({ html: "Please log in before adding item to cart." });
                } else {
                    M.toast({ html: product_name + "<br />was added to your cart!" });
                }
            },
            error: function (result) {
                M.toast({ html: "We're sorry,<br />something went wrong" });
            },
        });
    }
}

/**
 * Adds given product to given shopping cart, using an AJAX request.
 * @param {Number} shopping_cart_id ID of given shopping cart
 * @param {Number} product_id ID of given product
 */
function remove_from_shopping_cart(shopping_cart_id, product_id) {
    let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url: "/cart/ajax/remove_item/",
        method: "POST",
        data: {
            shopping_cart_id: shopping_cart_id,
            product_id: product_id,
            csrfmiddlewaretoken: csrftoken,
        },
        success: function (result) {
            if (result.message === 'REMOVED') {
                M.toast({ html: "Item removed from cart." });
                location.reload();
            } else {
                M.toast({ html: "We're sorry,<br />something went wrong" });
            }
        },
        error: function (result) {
            M.toast({ html: "We're sorry,<br />something went wrong" });
        },
    });
}

/**
 * Adds a GET parameter to the new_url global variable or removes if parameter already in new_url.
 * @param {String} text A new GET parameter for the URL
 */
function change_url(text) {
    if (!new_url.includes(text)) {
        if (new_url.includes("/?")) {
            new_url = new_url + "&" + text;
        } else {
            new_url = new_url + "?" + text;
        }
    } else {
        if (new_url[new_url.indexOf(text) - 1] === "?") {
            if (new_url.endsWith(text)) {
                new_url = new_url.replace("?" + text, "");
            } else {
                new_url = new_url.replace("?" + text + "&", "?");
            }
        } else {
            new_url = new_url.replace("&" + text, "");
        }
    }
}

/**
 * Changes URL to the new_url global variable, activating any parameters set by change_url().
 */
function go_to_url() {
    new_url = new_url.replace(/\?page=[0-9]&?/, "?");
    new_url = new_url.replace(/&page=[0-9]/, "");
    window.location = new_url;
}

var curr_url = window.location.href;
var new_url = curr_url;

// Ready dropdown
$(document).ready(function () {
    $(".dropdown-trigger").dropdown();
});

// Displays select
$(document).ready(function(){
    $('select').formSelect();
});

