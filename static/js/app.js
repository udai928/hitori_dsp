$(function(){
    $('input#request_json').on('click',function(){
        var json_obj = JSON.stringify($('textarea').val());
        $.ajax({
            type: "POST",
            url: "http://0.0.0.0:5000/post",
            data: json_obj,
            contentType: 'application/json',
            dataType: "json",
            success : function(json) {
			    console.log(json);
			    $('#result').text(json);
		    }
        });
    });
});
