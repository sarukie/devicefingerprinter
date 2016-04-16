import json
import requests
import base64
import random
from pprint import pprint


class FingerprintClient:
    def __init__(self):
        self.ACCOUNT_ID = '57116a4be4b0406b7fbcdbbb'
        self.REST_API_KEY = '05d7a5c1d39e6088'
        self.SITE_URL = "https://api3.siftscience.com/v3/accounts/{account_id}".\
            format(account_id=self.ACCOUNT_ID)

    def getSessionData(self, session_id):
        site_url, headers = self.\
            getRequest(
              "sessions",
              session_id)
        response = requests.get(site_url, headers=headers)
        return response.json()

    def getRequest(self, endpoint, endpoint_data, **kwargs):
      site_url = kwargs.get('url') or self.SITE_URL
      api_key = kwargs.get('api_key') or self.REST_API_KEY
      url = self.SITE_URL + '/' + endpoint + '/' + endpoint_data
      api_key = api_key + ':'
      headers = {"Authorization": "Basic {}".format(base64.b64encode(api_key.encode()).decode())}
      return (url, headers)


    def createOrder(self, user_id, session_id):
        # Sample $create_order event
        order = {
          # Required Fields
          "$type"             : "$create_order",
          "$api_key"          : "04ba0b585053921c",
          "$user_id"          : user_id,

          # Supported Fields
          "$session_id"       : session_id,
          "$order_id"         : "ORDER-" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1,32)),
          "$user_email"       : "someuser@example.org",
          "$amount"           : round(random.random() * 10000) * 1000,
          "$currency_code"    : "USD",
          "$billing_address"  : {
              "$name"         : user_id,
              "$phone"        : "1-415-555-6041",
              "$address_1"    : "2100 Main Street",
              "$address_2"    : "Apt 3B",
              "$city"         : "New London",
              "$region"       : "New Hampshire",
              "$country"      : "US",
              "$zipcode"      : "03257"
          },
          "$payment_methods"  : [
              {
                  "$payment_type"    : "$credit_card",
                  "$payment_gateway" : "$braintree",
                  "$card_bin"        : "542486",
                  "$card_last4"      : "4444"
              }
          ],
          "$shipping_address"  : {
              "$name"          : "Bill Jones",
              "$phone"         : "1-415-555-6041",
              "$address_1"     : "2100 Main Street",
              "$address_2"     : "Apt 3B",
              "$city"          : "New London",
              "$region"        : "New Hampshire",
              "$country"       : "US",
              "$zipcode"       : "03257"
          },
          "$expedited_shipping" : True,
          "$shipping_method"    : "$physical",
          "$items"             : [
            {
              "$item_id"        : "12344321",
              "$product_title"  : "Microwavable Kettle Corn: Original Flavor",
              "$price"          : 4990000, # $4.99
              "$upc"            : "097564307560",
              "$sku"            : "03586005",
              "$brand"          : "Peters Kettle Corn",
              "$manufacturer"   : "Peters Kettle Corn",
              "$category"       : "Food and Grocery",
              "$tags"           : ["Popcorn", "Snacks", "On Sale"],
              "$quantity"       : 4
            },
            {
              "$item_id"        : "B004834GQO",
              "$product_title"  : "The Slanket Blanket-Texas Tea",
              "$price"          : 39990000, # $39.99
              "$upc"            : "67862114510011",
              "$sku"            : "004834GQ",
              "$brand"          : "Slanket",
              "$manufacturer"   : "Slanket",
              "$category"       : "Blankets & Throws",
              "$tags"           : ["Awesome", "Wintertime specials"],
              "$color"          : "Texas Tea",
              "$quantity"       : 2
            }
          ],

          # For marketplaces, use $seller_user_id to identify the seller
          "$seller_user_id"     : "testingthisout",

          # Sample Custom Fields
          "digital_wallet"      : "apple_pay", # "google_wallet", etc. 
          "coupon_code"         : "dollarMadness",
          "shipping_choice"     : "FedEx Ground Courier",
          "is_first_time_buyer" : False
        }

        response = requests.post(
            "https://api.siftscience.com/v203/events",
            data=json.dumps(order),
            headers={"Content-type": "application/json"})


if __name__ == '__main__':
    foo = FingerprintClient()

    ''' Get the list of users attached to this session '''
    pprint(foo.getSessionData('316bf13920adcbb4ca3c3fa19f1c2042'))

    ''' create an order for the user id and the session '''
    foo.createOrder('monkeyfarts', '316bf13920adcbb4ca3c3fa19f1c2042')