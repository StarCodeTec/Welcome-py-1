from flask import Flask
from main import start_bot_true
application = Flask(__name__)

@application.route('/')
def run_script():
    return start_bot_true()

if __name__ == "__main__":
    application.run(debug=True)
