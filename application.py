from flask import Flask
from main import main_start
import asyncio as a
application = Flask(__name__)

@application.route('/')
def run_script():
    return a.run(main_start())

if __name__ == "__main__":
    application.run(debug=True)
