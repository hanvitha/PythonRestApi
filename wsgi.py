from flask import Flask, render_template
from flask_restful import Api
from Loan import Loan


app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return render_template('home.html')


api.add_resource(Loan, "/<string:name>")

if __name__ == '__main__':
    app.run()

