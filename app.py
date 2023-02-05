import sys
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

# THIS IS MODULAR PROGRAMMING

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("We testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
    
    logging.info("We are testing logging module")
    return "This is TESTING CI/CD pipeline"

@app.route("/test", methods=["GET", "POST"])
def test():
    return "CI/CD Test"

if __name__=='__main__':
    app.run(debug=True)

