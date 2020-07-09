$(document).ready(function () {
    granfPyBot.fetchMessages();


    $('#message-form').submit(function (e) {
        e.preventDefault();
        let message = $('#input-text').val();

        let text = { message };


        $('.old-chats').remove();

        granfPyBot.sendMessage(text);

        granfPyBot.onMessageReceived();

        $('#message-form').trigger('reset');
    });
});