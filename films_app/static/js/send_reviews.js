$(document).ready(() => {
    $('#reviewForm').submit(function(event) {
        event.preventDefault()
        console.log($(this).serialize())
        console.log($('#reviewForm'))
        $.ajax({
            type: 'post',
            data: $(this).serialize(),
            success: function(response){
                if (response.success){
                    $("#message").empty();
                    $("#message").html('<p style= "color: green;">' + response.message + '</p>');
                    $('#reviewForm')[0].reset();
                }
            },
            error: function(response){

            }
        })
    })
})