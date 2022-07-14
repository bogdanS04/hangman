import requests

URL = "https://opentdb.com/api.php?amount=10&category=19&type=boolean"

request = requests.get(url=URL)
request.raise_for_status()
question_data = request.json()['results']
