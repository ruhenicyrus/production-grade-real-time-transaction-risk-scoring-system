#checking the level of transaction risk
def checking_transaction_risk(transaction):
	if transaction["amount"]>500:
		return "VERY HIGH"
	elif transaction["amount"]>300:
		return"HIGH"
	else:
		return"LOW"

transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 350},
    {"id": 3, "amount": 800}
]
for txn in transactions:
	risk=checking_transaction_risk(txn)
	print("Transaction ID",txn["id"],"Risk is",risk)
