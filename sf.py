from simple_salesforce import Salesforce

class SfConnection():

    def __init__(self, username, password, security_token, isSandbox=False):
        print('attempting connection')
        self.salesforce = Salesforce(
            username=username,
            password=password,
            security_token=security_token,
            domain = 'test' if isSandbox else 'login'
        )
        print('connected')