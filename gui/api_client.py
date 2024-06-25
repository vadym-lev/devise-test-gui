import requests

BASE_URL = "http://127.0.0.1:8070/api_v1"


def get_statistics(sensor_type=None, operator=None, start_date=None, end_date=None):
    params = {}
    if sensor_type:
        params['sensor_type'] = sensor_type
    if operator:
        params['operator'] = operator
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date
    response = requests.get(f"{BASE_URL}/stat", params=params)
    response.raise_for_status()
    return response.json()


def create_test_result(test_result):
    response = requests.post(f"{BASE_URL}/test_result", json=test_result)
    response.raise_for_status()
    return response.json()


def delete_test_result(record_id):
    response = requests.delete(f"{BASE_URL}/test_result/{record_id}")
    response.raise_for_status()
    return response.json()

