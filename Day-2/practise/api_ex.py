import requests
import json

FACT_URL = "https://uselessfacts.jsph.pl/random.json"
JOKE_URL = "https://sv443.net/jokeapi/v2/joke/Any"


def info(mood):
    try:
        if mood == "joke":
            response = requests.get(JOKE_URL)
            response.raise_for_status()

            data = response.json()

            if data["type"] == "single":
                return data["joke"]
            else:
                return f"{data['setup']} - {data['delivery']}"

        elif mood == "fact":
            response = requests.get(FACT_URL)
            response.raise_for_status()

            data = response.json()
            return data["text"]

        else:
            return "please enter 'fact' or 'joke' only."

    except requests.exceptions.RequestException as e:
        return f"API Error: {e}"


user_input = input("fact or joke?: ").lower()
result = info(user_input)
print("\nResult:")
print(result)

with open("output.json", "w") as file:
    json.dump({"result": result}, file, indent=4)