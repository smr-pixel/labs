from datetime import datetime
import requests

url = 'https://api.nasa.gov/planetary/apod'
api_key = 'MdzhxzCxgq1CiBQfiWbbacGeCNdRa1OUaiVWuYE8'

def valid(date: str) -> bool:

    if not date:
        return False
    split = date.split('-')
    if len(split) != 3:
        return False
    year, month, day = split
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    start = '01-01-2015'
    if date < start:
        return False
    current = datetime.today().strftime('%Y-%m-%d')
    if date > current:
        return False
    return True

def get_apod(date = None):
    params = {'api_key': api_key}
    if date:
        params['date'] = date

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception('API request failed')
    
    return response.json()