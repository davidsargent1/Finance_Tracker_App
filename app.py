import datetime as dt


class SmartBudget:
    pass 

class BudgetBuckets:
    """
    Used for keeping track of multiple budget buckets
    attributes 
    self.buckets List of buckets
    """
    def __init__(self, buckets):
        self.buckets = buckets 


class BudgetBucket:
    """
    Used for keeping track of multiple expenses in a month
    Kept Ordered
    
    attributes:
    Transactions: List (sorted by date)
    Transaction either an Expense or an Income Source
    self.month: int from 1 - 12 representing  the month
    """
    def __init__(self, transactions, month):
        self.transactions = transactions
        self.month = month
    




class Expense:
    """ Used for tracking an expense, expense can be reccurent or single time
    attributes 
    reccur: boolean (T/F)
    date: Date 
    amt: dollar amount
    """
    def __init__(self, amt, date, reccur=False):
        self.amt = amt 
        self.date = date 
        self.reccur = reccur 
        
    def __repr__(self):
        return f"Expense({self.amt}, {self.date}, {self.reccur})"
 


class IncomeSource: 
    """ Tracks income after tax, date of deposit. Income can be a single deposit
    or a reccuring amount.
    reccur: boolean (T/F)
    date: Date of deposit
    amt: dollar amount of deposit
    name: name of income type
    """ 
    def __init__(self, date, amt, name, reccur=False):
        self.date = date
        self.amt = amt
        self.reccur = reccur
        self.name = name
    
    def __repr__(self):
        return f'Deposit: {self.name}, {self.amt}, {self.date}. Recurring: {self.reccur}'
    


    