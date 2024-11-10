from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def home():
    apod_data = get_apod(date=None)
    return render_template('home.html', apod=apod_data)

@app.route('/history', methods=['GET', 'POST'])
def history():
    apod_data = None
    error = None
    if request.method == 'POST':
        date = request.form['date']
        
        if not valid(date):
            error = 'An incorrect date or format was entered.'
            return render_template('history.html', error=error )
        
        try:
            apod=get_apod(date)
            return render_template('history.html', apod=apod, date=date, error=None)
        except Exception as e:
            error = f"Error retrieving data"
            return render_template('history.html', error=error)
        
    return render_template('history.html')
            

if __name__ == '__main__':
    app.run(debug=True)