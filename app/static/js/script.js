function submit_message(input_message) {
    // Call the ajax view in Flask via routes.py
    $.post('/search', { input_message: input_message }, handle_response);

    function handle_response(response) {
        // Display the location
        $(".chat-container").append(`
            <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                Bien sûr mon poussin ! La voici : ${response.address}     
            </div>
        `);
    }
}

$('#message-form').on('submit', function (e) {
    e.preventDefault();
    const input_message = $('#input_message').val()
    // Return if the user doesn't enter any text
    if (!input_message) {
        return
    }
    // Displays user message
    $('.chat-container').append(`
            <div class="chat-message col-md-5 human-message">
                ${input_message}
            </div>
        `)
    // Clear the message input 
    $('#input_message').val('')
    // Send the message
    submit_message(input_message)
});