from flask import Flask
import main as your_module

application = Flask(__name__)

@app.route('/')
def dynamic_page():
    return your_module.main()

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8000', debug=True)
