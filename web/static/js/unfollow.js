$(function() {
    let a = 1
    $('a').on('click', function(e) {
        let a = $(this).attr('id');
        $.post( "/unfollow/" + a);
        $(("#"+a.replace( /(:|\.|\[|\]|,|=|@)/g, "\\$1" ))+'_any').addClass("table-success");
        $("#"+a.replace( /(:|\.|\[|\]|,|=|@)/g, "\\$1" )).addClass("disabled");
        console.log(a);
    });
});