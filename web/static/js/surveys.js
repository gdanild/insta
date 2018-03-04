
jQuery(function($){
    if (voted == true){
        $.ajax({
            url: "/surveys/"+ window.survey_id,
            method: "POST",
            data: "ans=GET",
            dataType : "json",    
            success: function(data){
                for(let i = 0; i < data.id.length; i++){
                    document.getElementById("p" + data.id[i]).style.width = data.value[i];
                    document.getElementById("p" + data.id[i]).innerHTML = data.value[i];
                }
                window.voted = true;
            }
        })
    }
    $(".answer_cont").click(function(){
        if (window.voted == false){
        $.ajax({
            url: "/surveys/"+ window.survey_id,
            method: "POST",
            data: "ans="+this.id,
            dataType : "json",    
            success: function(data){
                for(let i = 0; i < data.id.length; i++){
                    document.getElementById("p" + data.id[i]).style.width = data.value[i];
                    document.getElementById("p" + data.id[i]).innerHTML = data.value[i];
                }
                window.voted = true;
            }
        })
    }
    });
});




