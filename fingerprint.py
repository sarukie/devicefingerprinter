import requests
import base64

class FingerprintClient:
    def __init__(self):
       self.ACCOUNT_ID = '57116a4be4b0406b7fbcdbbb'
       self.REST_API_KEY = '05d7a5c1d39e6088'
       self.SITE_URL = "https://api3.siftscience.com/v3/accounts/{account_id}".format(
          account_id=self.ACCOUNT_ID)

    def getSessionData(self, session_id):
        site_url, headers = self.getRequest("sessions", session_id) 
        response = requests.get(site_url, headers=headers)
        return response.json()

    def getRequest(self, endpoint, endpoint_data):
      site_url = self.SITE_URL + '/' + endpoint + '/' + endpoint_data
      api_key = self.REST_API_KEY + ':'
      headers = {"Authorization": "Basic {}".format(base64.b64encode(api_key.encode()).decode())}
      return (site_url, headers)

