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
        let searchTerm = $(this).val();
        updateModelsList(searchTerm);
    });
});