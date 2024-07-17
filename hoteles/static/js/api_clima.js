$(document).ready(function () {
    $("#consulta_clima_vina").click(function () {
        $('#clima_vina').empty();
        $.get("https://api.open-meteo.com/v1/forecast?latitude=-33.0246&longitude=-71.5518&current_weather=true",
            function (data) {
                var fecha = moment(data.current_weather.time).format('DD/MM/YYYY HH:mm');
                var temperatura = data.current_weather.temperature;
                var viento = data.current_weather.windspeed;
                $("#clima_vina").append("<li>" + fecha +
                    "</li><li>" + temperatura + "°C </li><li>" +
                    viento + " Km/h </li>")
            });

    });
});


$(document).ready(function () {
    $("#consulta_clima_santiago").click(function () {
        $('#clima_stgo').empty();
        $.get("https://api.open-meteo.com/v1/forecast?latitude=-33.4569&longitude=-70.6483&current_weather=true",
            function (data) {
                var fecha = moment(data.current_weather.time).format('DD/MM/YYYY HH:mm');
                var temperatura = data.current_weather.temperature;
                var viento = data.current_weather.windspeed;
                $("#clima_stgo").append("<li>" + fecha +
                    "</li><li>" + temperatura + "°C </li><li>" +
                    viento + " Km/h </li>")
            });

    });
});