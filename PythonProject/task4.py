class BankAccount:
    def __init__(self):
        self._balance = 0.0  # Приватный атрибут для хранения баланса
        self._transactions = []  # Приватный атрибут для хранения транзакций

    def deposit(self, amount):
        """Метод для внесения средств на счет."""
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self._balance += amount
        self._transactions.append(f"Депозит: +{amount:.2f}")
        print(f"Внесено {amount:.2f}. Новый баланс: {self._balance:.2f}")

    def withdraw(self, amount):
        """Метод для снятия средств со счета."""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            print("Ошибка: Недостаточно средств.")
            self._transactions.append(f"Попытка снятия: -{amount:.2f} (Недостаточно средств)")
            return False
        self._balance -= amount
        self._transactions.append(f"Снятие: -{amount:.2f}")
        print(f"Снято {amount:.2f}. Новый баланс: {self._balance:.2f}")
        return True

    @property
    def balance(self):
        """Геттер для получения текущего баланса."""
        return self._balance

    def get_transactions(self):
        """Метод для получения списка транзакций."""
        return self._transactions[:]



if __name__ == "__main__":
    acc = BankAccount()
    acc.deposit(1000)  # Внесение 1000
    acc.withdraw(250)   # Снятие 250
    acc.withdraw(900)   # Попытка снятия 900 (недостаточно средств)
    print(f"Текущий баланс: {acc.balance:.2f}")  # Вывод текущего баланса
    print("Транзакции:")
    for t in acc.get_transactions():  # Вывод всех транзакций
        print(t)