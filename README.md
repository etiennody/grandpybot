# GrandPy Bot !
App built for project 7 in Python developer path at Openclassrooms.

Here's a robot that would respond to you like your grandfather! If you ask him for the address of a place, he will give it to you, certainly, but with a long and very interesting story. Are you ready?

## Online application
https://grandpybot-geo-info.herokuapp.com/

## Requirements
* Python 3
* Flask
* Requests
* Gunicorn

## Setup
To run this application locally:

* Create a virtual environment. First, install pipenv:
    ```
    pip install --user pipenv
    ```

* Clone / create the application repository:
    ```
    git clone https://github.com/etiennody/grandpybot.git && cd grandpybot
    ```

* Copy and update environment variables values in .env:
    ```
    cp .env.example .env
    ```

* Add your own google maps and geocode api keys on .env:
    ```
    GOOGLE_GEOCODE_API_KEY="your_google_geocode_api_key"
    GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
    ```

* Install the requirements:
    ```
    pipenv install --dev
    ```

* Activate the pipenv shell:
    ```
    pipenv shell
    ```

* Run tests:
    ```
    pytest
    ```

* Run the GrandPy Bot application:
    ```
    python -m flask run
    ```

* Launch Flask server:
You can visit localhost at https://127.0.0.1:5000/

* Enjoy!!