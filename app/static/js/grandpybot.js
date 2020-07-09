const granfPyBot = function () {

    $('#empty-chat').hide();
    $('#group-message-holder').hide();

    let messageArray = [];

    if (messageArray.length < 1) {
        $('#empty-chat').show();
        $('#group-message-holder').hide();
    } else {
        $('#group-message-holder').show();
    }

    return {
        fetchMessages: function () {
            $.each(messageArray, function (index, value) {
                let messageList;
                messageList = `
                <div class="card mb-3 received-chats old-chats">
                <div class="card-body received-msg">
                    <div class="received-msg-inbox">
                        <p>${value.message}</p>
                    </div>
                </div>
                </div>                    
                    `
                $('#group-message-holder').append(messageList);
            });
            this.scrollToBottom();
        },
        sendMessage: function (message) {
            messageArray.push(message);
        },
        onMessageReceived: function () {
            $('#empty-chat').hide();
            $('#group-message-holder').show();

            $.each(messageArray, function (index, value) {
                let messageList;

                messageList = `
                <div class="card mb-3 received-chats old-chats">
                    <div class="card-body received-msg">
                            <div class="received-msg-inbox">
                                <p>${value.message}</p>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>                    
                `
                $('#group-message-holder').append(messageList);
            });
            this.scrollToBottom();
        },
        scrollToBottom() {
            const chat = document.getElementById("msg-page");
            chat.scrollTo(0, chat.scrollHeight + 30);
        }
    }
}();
