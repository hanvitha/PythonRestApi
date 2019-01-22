from flask import Flask
from flask_restful import Api
from Loan import Loan

app = Flask(__name__)
api = Api(app)
output = "Hello Welcome! <br> For loan details: URL/loan/accountHolderName <br> <b> examples </b><br> GET: <a> http://127.0.0.1:5000/loan/Jeremy </a> <br> POST: <a>http://127.0.0.1:5000/loan/Amy?amount=39000&duration=350 <a><br> PUT: <a>http://127.0.0.1:5000/loan/Jeremy?amount=39000&duration=350 </a><br>DELETE: <a> http://127.0.0.1:5000/loan/Joel</a><br>"
@app.route('/')
def hello_world():
    return output


api.add_resource(Loan, "/loan/<string:name>")

if __name__ == '__main__':
    app.run(debug=True)

