import requests
from urllib.parse import urljoin

BASE_URL = 'https://business-api.tiktok.com/open_api/v1.3/'


def convert_response(message, status_code, data=None):
    response = {
        "message": message,
        "code": status_code,
    }
    if data is not None:
        response.update({"data": data})
    return response


def create_campaign(data):
    create_loc = 'campaign/create/'
    create_url = urljoin(BASE_URL, create_loc)
    headers = {
        'Access-Token': '23d19996b998769044fca1251224c64e989675cb'
    }
    params = {
        'advertiser_id': data['advertiser_id'],
        'objective_type': data['objective_type'],
        'campaign_name': data['campaign_name'],
        'budget_mode': data['budget_mode'],
        'budget': data['budget'],
        'operation_status': data['operation_status'],
    }
    make_request = requests.post(url=create_url, data=params, headers=headers)
    campaign_json = make_request.json()
    return campaign_json
