class BankAccount:
    DOLLAR = 0
    EURO = 1
    SWISS_FRANC = 2

    def __init__(self, currency_type, amount):
        self.currency_type = currency_type
        self.amount = amount

    def add(self, added_type, added_amount):
        in_currency = 0
        if self.currency_type == added_type:
            in_currency = added_amount
        elif self.currency_type == BankAccount.DOLLAR and added_type == BankAccount.EURO:
            in_currency = 1.15 * added_amount
        elif self.currency_type == BankAccount.DOLLAR and added_type == BankAccount.SWISS_FRANC:
            in_currency = 0.95 * added_amount
        elif self.currency_type == BankAccount.EURO and added_type == BankAccount.DOLLAR:
            in_currency = 0.87 * added_amount
        elif self.currency_type == BankAccount.EURO and added_type == BankAccount.SWISS_FRANC:
            in_currency = 0.83 * added_amount
        elif self.currency_type == BankAccount.SWISS_FRANC and added_type == BankAccount.DOLLAR:
            in_currency = 1.05 * added_amount
        elif self.currency_type == BankAccount.SWISS_FRANC and added_type == BankAccount.EURO:
            in_currency = 1.2 * added_amount
        self.amount += in_currency
        return True

    def remove(self, removed_type, removed_amount):
        in_currency = 0
        if self.currency_type == removed_type:
            in_currency = removed_amount
        elif self.currency_type == BankAccount.DOLLAR and removed_type == BankAccount.EURO:
            in_currency = 1.15 * removed_amount
        elif self.currency_type == BankAccount.DOLLAR and removed_type == BankAccount.SWISS_FRANC:
            in_currency = 0.95 * removed_amount
        elif self.currency_type == BankAccount.EURO and removed_type == BankAccount.DOLLAR:
            in_currency = 0.87 * removed_amount
        elif self.currency_type == BankAccount.EURO and removed_type == BankAccount.SWISS_FRANC:
            in_currency = 0.83 * removed_amount
        elif self.currency_type == BankAccount.SWISS_FRANC and removed_type == BankAccount.DOLLAR:
            in_currency = 1.05 * removed_amount
        elif self.currency_type == BankAccount.SWISS_FRANC and removed_type == BankAccount.EURO:
            in_currency = 1.2 * removed_amount
        if in_currency > self.amount:
            return False
        self.amount -= in_currency
        return True

if __name__ == "__main__":
    account = BankAccount(BankAccount.EURO, 9001)
    account.add(BankAccount.DOLLAR, 100)
    account.add(BankAccount.SWISS_FRANC, 10)
    print(account.amount)
