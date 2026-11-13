
class Expense:

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print(
            "Amount:", self.amount,
            "| Category:", self.category,
            "| Description:", self.description
        )

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description
        }
