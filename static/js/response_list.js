var timeout;

$(document).ready(function() {
    function updateModelsList(searchTerm) {
        $.ajax({
            url: responseListUrl,
            data: { filter: searchTerm },
            success: function(data) {
                $('#response_list').html($(data).html());
            }
        });
    }

    $('#filter').on('input', function() {
        if(timeout) clearTimeout(timeout);

        timeout = setTimeout(function (){
            let searchTerm = $("#filter").val();
            updateModelsList(searchTerm);
        }, 200)
    });
});