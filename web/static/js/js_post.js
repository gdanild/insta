$(function() {
    $('img').hide();
    let a = 1
    $('button').on('click', function(e) {
        $(this).hide()
        console.log("LOL");
        $('img').show();
    });
});