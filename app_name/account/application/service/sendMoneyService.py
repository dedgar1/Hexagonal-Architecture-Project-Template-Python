from app_name.account.application.port.input.SendMoneyUseCase import SendMoneyUseCase


class SendMoneyService(SendMoneyUseCase):
    def __init__(self, loadAccountPort, accountLock, updateAccountStatePort):
        self.loadAccountPort = loadAccountPort
        self.accountLock = accountLock
        self.updateAccountPort = updateAccountStatePort

    def sendMoney(sendMoneyCommand):
        pass
