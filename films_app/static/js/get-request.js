$(document).ready(function(){
    $('.filter').each(function(){
        $(this).on('click', function(){
            let value = $(this).val()
            console.log(value)
            $.ajax({
                url: `/films/get-by-filter/` + value,
                type: 'get',
                success: function(response){
                    console.log(response)
                    $(".all-films").empty();
                    let htmlc = ''
                    for (let counter = 0; counter < response.films.length; counter++){
                        htmlc += `<hr>`
                        htmlc += `<p>${response.films[counter].name}</p>`
                        htmlc += `<p>${response.films[counter].description}</p>`
                        htmlc += `<img src='/media/${response.films[counter].image}'/>`
                        htmlc += `<p>${response.films[counter].genre}</p>`
                        htmlc += `<hr>`
                    }    
                    $(".all-films").html(htmlc)
                }
            })
        })
    })
})