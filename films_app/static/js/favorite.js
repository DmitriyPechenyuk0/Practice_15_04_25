$(document).ready(function(){
    let favouriteNumber = $("#count")
    let count
    $('.Add-To-Favourite').each(function(){
        $(this).on("click", function(){
        $.ajax({
            url: $(this).val(),
            type: 'get',
            success: function(response){
                // console.log(favouriteNumber.text());
                count = favouriteNumber.text();
                // console.log(+count);
                +count++;
                // console.log(count);
                favouriteNumber.text(count);
            }
            })
        })
    })
})
// Декоратор в jquery
// $()
// Декоратор в Python
// @document.ready()
// def main1():
//     pass
// Задіюємо метод до декоратору
// $(document).ready(function(){

// })