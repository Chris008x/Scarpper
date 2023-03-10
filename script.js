$(document).ready(function() {
    $("#search-form").submit(function(event) {
        event.preventDefault();
        var city = $("#city").val();
        var type = $("input[name='type']:checked").val();
        var query = type + "+near+me+" + city;
        $.get("search.py?q=" + query, function(data) {
            $("#results").html(data);
        });
    });
});
