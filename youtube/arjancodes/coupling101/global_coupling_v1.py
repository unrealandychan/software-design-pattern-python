# These are all dummy code, the API Key and Account ID are not real.

API_ULR = "https://api.github.com"
API_VERSION_ID = "v3"
TOKEN = "ghp_4r3v1n7x2c0g5e8f3d2a4b5c6d7e8f9a0b1c2"
ACCOUNT_ID = "arjancodes"

type JSONDict = dict[str, str|int|float|bool|list|dict]

# But now this is the data coupling problem, we need to pass the API URL, API version, and account ID as parameters to the function.
# How to solve this problem?
def make_request (
        api_url:str ,
        api_version:str ,
        path:str,
        token:str,
        account_id:int,
        data: JSONDict|None= None,
        method:str = "POST" )->None:
    headers = {"Authorization": f"token {token}",
                "Accept": f"application/vnd.github.{api_version}",
                "Content-Type": "application/json"}
    full_url = f"{api_url}/{api_version}/{account_id}/{path}"
    print(f"Making {method} request to {full_url}")
    print(f"Data: {data}")
    print(f"Method: {method}")
    print(f"Headers: {headers}")

def main ()-> None:
    path = "repos/arjancodes/coupling101/issues"
    data = {"title": "New issue", "body": "This is a new issue"}
    make_request(API_ULR, API_VERSION_ID, path, TOKEN, ACCOUNT_ID, data, method="POST")