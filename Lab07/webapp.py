from flask import Flask, render_template, request
import segno
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_data = None
    message = None
    
    if request.method == 'POST':
        message = request.form['data']
        if message:
            qr = segno.make(message)
            buffer = io.BytesIO()
            qr.save(buffer, kind='png', scale = 4, dark = 'hotpink')  # Save as PNG to buffer
            qr_code_data = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return render_template('index.html', qr_code_data=qr_code_data, message=message)

if __name__ == '__main__':
    app.run(debug=True)
