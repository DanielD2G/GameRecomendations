import openai
import json as j
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv('API_KEY')


def obtain_recommendation(game_list, number, except_recomendations=None) -> dict:
    json_format = {
        "recommendations": [
            {
                "name": "",
                "genre": "",
                "description": "",
                "platforms": [""]
            }
        ]
    }

    prompt = f"Return {number} game recommendations based in {game_list} skip prequels or sequels, " \
             f"skip games related to {except_recomendations}, in a json formatted like this {json_format}"

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                              messages=[{"role": "user", "content": f"{prompt}"}])

    json = j.loads(completion.choices[0].message.content)

    return json



