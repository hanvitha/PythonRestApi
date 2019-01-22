from flask_restful import Resource, reqparse
from LoanAccounts import loanAccounts

class Loan(Resource):
    def get(self, name):
        for account in loanAccounts:
            if name == account["name"]:
                return "Hello {}, Your loan amount is : {}, and duration {}".format(name, account["amount"], account["duration"]), 200
        return "No Loan Account found!", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("amount")
        parser.add_argument("duration")
        args = parser.parse_args()

        for account in loanAccounts:
            if name == account["name"]:
                return "Loan account holder {} already exists".format(name), 400

        newAccount = {
            "name" : name,
            "amount" : args["amount"],
            "duration" : args["duration"]
        }
        loanAccounts.append(newAccount)
        return newAccount, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("amount")
        parser.add_argument("duration")
        args = parser.parse_args()

        for account in loanAccounts:
            if name == account["name"]:
                account["amount"] = args["amount"]
                account["duration"] = args["duration"]
                return account, 200

        newAccount = {
            "name": name,
            "amount": args["amount"],
            "duration": args["duration"]
        }
        loanAccounts.append(newAccount)
        return newAccount, 201

    def delete(self, name):
        global loanAccounts
        loanAccounts = [account for account in loanAccounts if account["name"] != name]
        return "{} is deleted.".format(name), 200



