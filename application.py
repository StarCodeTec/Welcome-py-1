from flask import Flask

application = Flask(__name__)

@application.route('/')
def run_script():
    file = open(r'./main.py', 'r').read()
    return exec(file)

if __name__ == "__main__":
    application.run(debug=True)
