# Flask Rest API Testing

## Usage

To use this repository you will need:
- Python 3.10

1. Create a virtual environment and install the package into it:
    ```bash
   python -m venv --prompt . .venv
   .venv/bin/activate
   pip install .
    ```
2. Run the app locally in debug mode
    ```bash
    flask --app flask_rest_test run --debug
    ```
    Visit http://127.0.0.1:5000 to view the app

3. POST data to the app. 
   You can add sandwiches to the app using HTTP POST requests with a tool such as curl.
    ```bash
    curl -X POST http://127.0.0.1:5000/add  \
         -H 'Content-Type: application/json' \
         -d '{"name":"marmite and cheese","count":11}'
   ```
   