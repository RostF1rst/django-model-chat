$(document).ready(function() {
    var loading = false;

    $('#loading').hide();
    $('#prompt-message').hide();
    $('#post-response').hide();

    $('#prompt-form').on('submit', function(event) {
        event.preventDefault();
        if (loading) {
            return;
        }
        let promptForm = $('#prompt-form')
        let responseMessage = $('#response-message')
        let promptMessage = $('#prompt-message')

        let inputText = promptForm.find('#prompt').val();
        let real = promptForm.find('#real').is(':checked')
        let csrfToken = promptForm.find('input[name=csrfmiddlewaretoken]').val()

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

                $('#post-response').hide();

                promptForm.find('#prompt').val('')

                responseMessage.find('#content').hide()
                responseMessage.find('#loading').show()
                promptMessage.find('#content').text(inputText)
                promptMessage.show()
            },
            success: function(response) {
                loading = false;
                if (response.error) {
                    alert(response.error);
                } else {
                    $('#prompt-value').val(inputText)
                    $('#response-value').val(response.response)
                    $('#post-response').show()

                    responseMessage.find('#content').text(response.response)
                    responseMessage.find('#content').show()
                    responseMessage.find('#loading').hide()
                }
            },
            error: function() {
                loading = false;
                alert('An error occurred.');
            }
        });
    });
});