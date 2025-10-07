from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>🎉 Hello World!</h1>
            <p>This app is protected by IAP</p>
            <p>If you can see this, you have access!</p>
        </body>
    </html>
    '''

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
