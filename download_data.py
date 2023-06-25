import requests

class Download:
    def __init__(self) -> None:
        """
        Initializes a Download object.
        """
        pass

    def iss_api(self):
        """
        Makes an API request to retrieve information about the International Space Station (ISS).

        Returns:
            list: A list of values extracted from the API response.
        """
        iss = requests.get('https://api.wheretheiss.at/v1/satellites/25544').json()
        values = iss.values()

        list_values = []
        for value in values:
            list_values.append(value)

        return list_values