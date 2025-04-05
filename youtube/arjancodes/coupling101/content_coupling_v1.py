from dataclasses import dataclass
from enum import StrEnum, auto

class PaymentType(StrEnum):
    CASH = auto()
    CREDIT = auto()
    DEBIT = auto()

SERVICE_FEE = {
    PaymentType.CASH: 50,
    PaymentType.CREDIT: 100,
    PaymentType.DEBIT: 150
}


@dataclass
class Account:
    owner: str
    _balance: int = 0

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
        print(f"Deposited {amount} to {self.owner}'s account. New balance: {self._balance}")

    def withdraw(self, amount: int) -> None:
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to balance")
        print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self._balance}")

    @property
    def balance(self) -> int:
        return self._balance

    def pay_service_fee(self, payment_type: PaymentType) -> None:
        self._balance -= SERVICE_FEE[payment_type]  # This is invalid
        print(f"Paid service fee of {SERVICE_FEE[payment_type]} using {payment_type}. New balance: {self.balance}")


def main() -> None:
    account = Account(owner="John Doe")
    account.deposit(1000)
    account.withdraw(200)
    print(f"Final balance: {account.balance}")

    account.pay_service_fee(PaymentType.CASH)
    print(f"Final balance after service fee: {account.balance}")

if __name__ == "__main__":
    main()