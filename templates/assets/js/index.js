$(document).ready(function() {
    $('#generate-button').click(function(e){
        e.preventDefault();
        var original_title = $("#original_title").val();
        var comparing_titles = $("#comparing_titles").val();

        $('#results').html("");

        axios.post(`/api/compare/`, {original : original_title, comparing: comparing_titles}).then(function (response) {
            var result = response.data.result;
            // for each item in result, put a new line and append to #results
            result.forEach(function(item){
                $('#results').append(item['title'] + ": " + item['similarity'] + "<br>");
            });
        });
    });
})