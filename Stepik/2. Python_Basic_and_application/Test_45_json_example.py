import json

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    },
    "resea": {
    "name": "Ford Prefect",
    "species": "Betelgeusian",
    "relatives": [
        {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    ]
    }
}
"""

data = json.loads(json_string)

for i in data:
    print(i)
