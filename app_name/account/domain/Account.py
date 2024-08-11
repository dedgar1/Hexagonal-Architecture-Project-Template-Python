class Account:
    def __init__(self, accountId: int, baselineBalance: int, activityWindow: int):
        self.accountId = accountId
        self.baselineBalance = baselineBalance
        self.actvityWindow = activityWindow

    def calculateBalance(self) -> int:
        return self.baselineBalance

    def withdrawMoney(self, money: int, targetAccountId: int) -> int:
        if self.baselineBalance < money:
            return False
        return True
