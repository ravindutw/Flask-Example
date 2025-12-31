from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/get', methods=['GET'])
def get_data():
    return "This is the return from the API."


if __name__ == '__main__':
    app.run(debug=True)

