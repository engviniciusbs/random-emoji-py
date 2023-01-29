document.getElementById("refresh-button").addEventListener("click", function(){
    fetch('/refresh_image')
        .then(response => response.text())
        .then(image => {
            let img = document.getElementById('image');
            img.src = '/static/images/' + image;
        });
});

$(document).ready(function(){
    $("#checkbox").click(function(){
        if($("#theme-link").attr("href") === "../static/css/light-theme.css"){
            $("#theme-link").attr("href", "../static/css/dark-theme.css");
        } else {
            $("#theme-link").attr("href", "../static/css/light-theme.css");
        }
    });
});
