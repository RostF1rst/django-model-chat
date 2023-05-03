$(document).ready(function() {
    var loading = false;

    $('#prompt-form').on('submit', function(event) {
        event.preventDefault();
        if (loading) {
            return;
        }
        let inputText = $('#prompt').val();
        let real = $('#real').is(':checked')
        let csrfToken = $('#prompt-form').find('input[name=csrfmiddlewaretoken]').val()
        $.ajax({
            type: 'POST',
            url: responseUrl,
            data: {
                csrfmiddlewaretoken: csrfToken,
                prompt: inputText,
                real: real
            },
            dataType: 'json',
            beforeSend: function() {
                loading = true;
                $('#prompt').val('')
                $('#post-response').hide()
                $('#welcoming-text').hide()
                $('#response-blank').show()
                $('#response-text').text('Loading...')
            },
            success: function(response) {
                loading = false;
                if (response.error) {
                    alert(response.error);
                } else {
                    $('#post-response').show()
                    $('#response-text').text(response.response)
                    $('#prompt-value').val(inputText)
                    $('#response-value').val(response.response)
                }
            },
            error: function() {
                loading = false;
                alert('An error occurred.');
            }
        });
    });
});