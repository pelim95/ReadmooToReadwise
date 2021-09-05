import requests
import logging


def add_into_readwise(token, highlight_jsons):
    try:
        response = requests.post(
            url="https://readwise.io/api/v2/highlights/",
            headers={"Authorization": "Token " + token},
            json={
                "highlights": highlight_jsons
            }
        )
        if response.status_code != 200:
            logging.error('Error importing highlights to Readwise: ' + str(response.status_code))
            raise Exception(response.status_code)

        return response.status_code
    except Exception as ex:
        logging.error('Error importing highlights to Readwise: ' + str(ex))
        return response.status_code
