import requests

class ProvenancedRepository:
    """ The repository for the provenance model """

    @staticmethod
    def getStatus():
        provStatus = requests.get('http://localhost:26657/status')
        return provStatus.json()
    
    @staticmethod
    def getNetworkInfo():
        netInfo = requests.get('http://localhost:26657/net_info')
        return netInfo.json()

