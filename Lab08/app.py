from flask import Flask, render_template, request
from apod import get_apod, valid

app = Flask(__name__)

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