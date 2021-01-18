from simple_salesforce import Salesforce

class SfConnection():

    def __init__(self, username, password, security_token, isSandbox):
        self.salesforce = Salesforce(
            username="ahess@nnb.com.custondev",
            password="SoCasual#1",
            security_token="agrzEf7V1xHNm3LLCyre4Gqp6",
            domain="test"
        )

    def query(self, query):
        return self.salesforce.query(query)