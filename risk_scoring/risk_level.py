import sqlite3

connection = sqlite3.connect("../transactions.db")
cursor = connection.cursor()

def checking_transaction_risk(transaction):
    if transaction["amount"] > 500:
        return "VERY HIGH"
    elif transaction["amount"] > 300:
        return "HIGH"
    else:
        return "LOW"

transactions = [
    {"id": 1, "amount": 100},
    {"id": 2, "amount": 350},
    {"id": 3, "amount": 800}
]

for txn in transactions:
    risk = checking_transaction_risk(txn)

    cursor.execute(
        "INSERT INTO transactions (amount, risk_level) VALUES (?, ?)",
        (txn["amount"], risk)
    )

    print(
        "Transaction ID",
        txn["id"],
        "Amount",
        txn["amount"],
        "Risk",
        risk,
        "→ STORED"
    )

connection.commit()
connection.close()
