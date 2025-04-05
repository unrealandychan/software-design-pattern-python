from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum, auto
from typing import Protocol

class TransactionType(StrEnum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()
    INTEREST = auto()

class Loggable(Protocol):
    transaction_type: TransactionType
    transaction_id: int
    timestamp: datetime
    amount: int
    customer_id: int

# That will be a problem if the transaction class change in the future.
# So we need to decouple the transaction class from the process_transaction function.
@dataclass
class Transaction:
    transaction_id :int
    transaction_type : TransactionType
    amount :int # I make that a int as it is simple to understand
    timestamp : datetime
    customer_id : int

def log_transaction(transaction:Loggable) -> None:
    print(f"Transaction ID: {transaction.transaction_id}")
    print(f"Transaction Type: {transaction.transaction_type}")
    print(f"Amount: {transaction.amount}")
    print(f"Timestamp: {transaction.timestamp}")
    print(f"Customer ID: {transaction.customer_id}")
    print("----------------------------")

def process_transaction(transaction: Transaction) -> None:
    log_transaction(transaction)
    if transaction.transaction_type == TransactionType.DEPOSIT:
        print(f"Deposited {transaction.amount} to account.")
    elif transaction.transaction_type == TransactionType.WITHDRAWAL:
        print(f"Withdrew {transaction.amount} from account.")
    elif transaction.transaction_type == TransactionType.INTEREST:
        print(f"Applied interest of {transaction.amount} to account.")
    else:
        raise ValueError("Invalid transaction type")

def main() -> None:
    transaction1 = Transaction(
        transaction_id=1,
        transaction_type=TransactionType.DEPOSIT,
        amount=1000,
        timestamp=datetime.now(),
        customer_id=12345
    )

    transaction2 = Transaction(
        transaction_id=2,
        transaction_type=TransactionType.WITHDRAWAL,
        amount=500,
        timestamp=datetime.now(),
        customer_id=12345
    )

    process_transaction(transaction1)
    process_transaction(transaction2)

if __name__ == "__main__":
    main()