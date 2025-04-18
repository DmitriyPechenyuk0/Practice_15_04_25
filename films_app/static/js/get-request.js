$(document).ready(function(){
    $('.filter').each(function(){
        $(this).on('change', function(){
            let acgenres = []
            
            $('.filter:checked').each(function(){
                acgenres.push($(this).val())
            })

            let value = $(this).val()
            
            console.log(value)

            $.ajax({
                url: `/films/get-by-filter/`,
                type: 'get',
                data: {
                    genres: acgenres.join('-')
                },
                success: function(response){
                    console.log(response)
                    $(".all-films").empty();
                    let htmlc = ''
                    for (let counter = 0; counter < response.films.length;){
                        htmlc += `<hr>`
                        htmlc += `<p>${response.films[counter].name}</p>`
                        htmlc += `<p>${response.films[counter].description}</p>`
                        htmlc += `<img src='${response.films[counter].image}'/>`
                        htmlc += `<p>${response.films[counter].genre}</p>`
                        htmlc += `<hr>`
                        counter++
                    }

                    $(".all-films").html(htmlc)
                }
            })
        })
    })
})