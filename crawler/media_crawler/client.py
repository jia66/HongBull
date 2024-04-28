from xmlrpc.client import ServerProxy
import time

server_url = "http://localhost:8000/"

def call_rpc(method: function, retry_times: int = 3, sleep_time: int = 2):
    """
    Call RPC method with retry
    """
    for i in range(retry_times):
        try:
            with ServerProxy(server_url) as proxy:
                return method(proxy)
        except Exception as e:
            print(e)
            time.sleep(sleep_time)