$(document).ready(function(){
    $('.filter').each(function(){
        $(this).on('click', function(){
            let value = $(this).val()
            $.ajax({
                type: 'get',
                success: function(response){
                    $(".all-films").empty();
                    $(".all-films").html('<p>' + value + '</p>');
                }
            })
        })
    })
})