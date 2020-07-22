//map variables
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
            return true
        }

        let address = response.address;
        let lat = response.lat;
        let lng = response.lng;
        let wiki_extract = response.wiki_extract;


        // Display the location address
        $(".chat-container").append(`
            <div class="chat-message col-md-5 offset-md-7 grandpybot-message">
                Bien sûr mon poussin ! La voici : ${address}     
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
                    ${wiki_extract}
                </div>
            `);
        };
        show_wiki()
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