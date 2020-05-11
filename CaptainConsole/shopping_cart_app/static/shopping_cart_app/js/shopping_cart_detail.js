var removeCartItemButtons = document.getElementsByClassName('delete-cross');

for (var i = 0; i < removeCartItemButtons.length; i++) {
    var button = removeCartItemButtons[i];
    button.addEventListener('click', function(event) {
       var buttonClicked = event.target;
       buttonClicked.parentElement.remove()
    });
}