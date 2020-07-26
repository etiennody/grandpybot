//Map variables
let address;
let map;
let marker;
let mapIndex;
let index = 0;
function initMap(lat, lng, address) {
    // Create map object
    map = new google.maps.Map(document.getElementById(mapIndex), {
        center: { lat: lat, lng: lng },
        zoom: 16
    });
    marker = new google.maps.Marker({
        position: { lat: lat, lng: lng },
        map: map
    });
    // Display info on click
    let infowindow = new google.maps.InfoWindow({
        content: address
    });
    marker.addListener('click', function () {
        infowindow.open(map, marker);
    });
    index += 1;
}

function submit_message(input_message) {
    // Call the ajax view in Flask via routes.py
    $.post('/search', { input_message: input_message }, handle_response);

    function handle_response(response) {
        if (response.error) {
            $(".chat-container").append(`
            <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                ${response.error}     
            </div>
            `);

            // Remove the loading indicator
            $("#loading").remove();

            return true
        }
        
        let address_reply = response.address_reply
        let address = response.address;
        let lat = response.lat;
        let lng = response.lng;
        let wiki_reply = response.wiki_reply;


        // Display the location address
        $(".chat-container").append(`
            <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                ${address_reply}     
            </div>
        `);

        function show_map() {
            mapIndex = "map" + String(index);
            // Display the location map
            $(".chat-container").append(`
                <div id=${mapIndex} class="map">
                </div>
            `);

            //Create map with coordinates
            initMap(lat, lng, address);
        };
        show_map()

        function show_wiki() {

            $(".chat-container").append(`
                <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                    ${wiki_reply}
                </div>
            `);
        };
        show_wiki()

        // Remove the loading indicator
        $("#loading").remove();
    }
    this.scrollToBottom();
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

    // Loading 
    $('.chat-container').append(`
        <div class="chat-message text-center col-md-5 offset-md-7 grandpybot-message" id="loading">
            <i class="fas fa-sync fa-spin fa-3x fa-fw"></i>
        </div>
        
    `)

    // Clear the message input 
    $('#input_message').val('')
    // Send the message
    submit_message(input_message)
});

function scrollToBottom() {
    const chat = $('.chat-container');
    chat.scrollTop(chat[0].scrollHeight);
}
scrollToBottom();
setInterval(scrollToBottom, 8000);