def calculate_summary(records):
    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")
    balance = income - expense
    return {
        "total_income":income,
        "total_expense":expense,
        "balance":balance
    }