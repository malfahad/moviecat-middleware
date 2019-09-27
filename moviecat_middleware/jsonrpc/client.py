
from ..settings import JSON_RPC_SERVER_URL
import requests, json

class JSONRpcClient():  
    def __init__(self):
         self._headers = {'content-type': 'application/json'}
   
    def create_movie(self, id, params):
        payload = {
        "method": "echo",
        "params": params,
        "jsonrpc": "2.0",
        "id": id,
        }
        return self._make_request(payload)


    def _make_request(self, payload):
        return requests.post(
                JSON_RPC_SERVER_URL, 
                data=json.dumps(payload),
                 headers=self._headers).json()
    

jsonrpc_client = JSONRpcClient()
