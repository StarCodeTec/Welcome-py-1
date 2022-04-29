from flask import Flask
from main import main
import asyncio as a
application = Flask(__name__)

@application.route('/')
def run_script():
    return a.run(main())

if __name__ == "__main__":
    application.run(debug=True)
