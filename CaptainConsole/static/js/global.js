/**
 * Function makes an AJAX request which adds
 * a given quantity of the product to the users shopping cart.
 * @param {String} product_id ID of the given product
 * @param {String} product_name Name of the given product
 */
function add_to_shopping_cart(product_id, product_name) {
    let quantity = Number(document.getElementById('quantity').value)
    if (quantity > 0) {
        let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: "/store/ajax/add_product_to_cart/",
            method: "POST",
            data: {
                product_id: product_id,
                quantity: quantity,
                csrfmiddlewaretoken: csrftoken
            },
            success: function (result) {
                M.toast({ html: product_name + "<br />was added to cart!" });
            },
            error: function (result) {
                M.toast({ html: "We're sorry,<br />something went wrong" });
            }
        });
    }
}
