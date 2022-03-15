question_data = []

import requests

data = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean").json()

for result in data['results']:
    question_data.append(result)
