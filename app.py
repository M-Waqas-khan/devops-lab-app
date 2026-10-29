from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>DevOps Class Activity: Docker & GitHub Actions Pipeline Active!</h1>'
    return '<p>Hurrah! Muhammad Waqas has Done his Class Activity-03 <br>Welcome to the DevOps Class Activity!</p>'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)