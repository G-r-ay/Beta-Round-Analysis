import requests
import json
import pandas as pd 
covalent_api_key = 'ckey_74166d4ccdcf4477926519d28cb'
session = requests.Session() 
session.auth = (covalent_api_key, '') 



def TDD(address):
    """
    ## TDD System.
    
    Args:
        address (string): Description of the first argument.

    Returns:
        True or False.

    Usage:
    ```
    On_chain_Footprint_Lego('0x2000fe4707df0e72b72f92753cfc237fc26248c6')
    >>> True
    ```
    """
#--------------------------------------------------------------------------------------------------------------------------------------
    def get_txn_count(address):
        pokt_fantom_endpoint = "https://eth-mainnet.gateway.pokt.network/v1/lb/78cad988d47e553027481226"
        headers = {'content-type': 'application/json'}

        payload = {
            "method": "eth_getTransactionCount",
            "params": [address, "latest"],
            "jsonrpc": "2.0",
            "id": 1,
        }
        response = requests.post(pokt_fantom_endpoint, data=json.dumps(payload), headers=headers).json()
        transaction_count = int(response['result'], 16)
        return transaction_count
#--------------------------------------------------------------------------------------------------------------------------------------

    def txn_dates(address):
        transaction_dates = []
        url = f"https://api.covalenthq.com/v1/1/address/{address}/transactions_v2/?no-logs=True"
        
        headers = {
            "x-api-key": covalent_api_key
        }
    
        response = session.get(url, headers=headers)
        txn_data = response.json()['data']['items']
        for index in range(len(txn_data)):
            transaction_dates.append(txn_data[index]['block_signed_at'])
        transaction_dates.reverse()
        transaction_dates = pd.to_datetime(pd.Series(transaction_dates))
        return transaction_dates

#--------------------------------------------------------------------------------------------------------------------------------------
    dates = txn_dates(address)
    txn_count = get_txn_count(address)
    date_diff = []
    for date in range(1, len(dates)):
        diff = (dates[date] - dates[date-1]).days
        date_diff.append(diff)
    TDD = (sum(date_diff)/txn_count)

    return TDD,txn_count



