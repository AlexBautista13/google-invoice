class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f' {self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client
    
    @property
    def total(self):
        return self._total


google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)