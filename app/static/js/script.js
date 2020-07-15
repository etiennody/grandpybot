function submit_message(message) {
    $.post("/search", { message: message }, handle_response);

    function handle_response(data) {
        // append the grandpybot response to the div
        $('.chat-container').append(`
            <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                ${data.message}
            </div>
      `)
    }
}

$('#message-form').on('submit', function (e) {
    e.preventDefault();
    const input_message = $('#input_message').val()
    // return if the user doesn't enter any text
    if (!input_message) {
        return
    }

    $('.chat-container').append(`
        <div class="chat-message col-md-5 human-message">
            ${input_message}
        </div>
    `)

    // clear the text input 
    $('#input_message').val('')

    // send the message
    submit_message(input_message)
});