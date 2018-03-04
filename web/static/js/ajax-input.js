(function () {
    let photo = ''
    $("#change_av").on("click", function () {
        $(".dark-screen").show();
        $(".change-foto").removeClass("change-foto-hidden");
    });
    $("#cancel_btn").on("click", function(){
        $(".dark-screen").hide();
        $(".change-foto").addClass("change-foto-hidden");
        $("#upload_btn").addClass("disabled");
        $("#preview")[0].style.backgroundImage =  $("#main_ava")[0].style.backgroundImage;
    });
    $(".sel-btn").on("change", function(){
        let file = $("#file_inp")[0].files[0];
        let data = new FormData();
        data.append('file', file)
        $.ajax({
            url:'ajax/image', 
            type:'POST',
            data: data,
            cache: false, 
            processData : false,
            contentType : false,
            success:function(data, textStatus){
                photo = data;
                $("#preview")[0].style.backgroundImage = "url(static/upload/" + data + ")";
                $("#upload_btn").removeClass("disabled");
            }

        });
    });
    $("#upload_btn").on('click', function(){
        if($(this).hasClass('disabled')) return;
        $("#main_ava")[0].style.backgroundImage = "url(static/upload/" + photo + ")";
        $.ajax({url:'/ajax/ava_success', type:'GET',data:'photo='+photo});
        $(".dark-screen").hide();
        $(".change-foto").addClass("change-foto-hidden");
        $("#upload_btn").addClass("disabled");
        
    });
})();