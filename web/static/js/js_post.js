$(function() {
    $('.progress').hide();
    let a = 1
    $('button').on('click', function(e) {
        $(this).hide()
        console.log("LOL");
        $('.progress').show();
        $('.g-recaptcha').hide()
        $('.alert alert-warning').hide()
    });
});