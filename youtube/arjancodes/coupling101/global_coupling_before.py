# These are all dummy code, the API Key and Account ID are not real.

API_ULR = "https://api.github.com"
API_VERSION_ID = "v3"
TOKEN = "ghp_4r3v1n7x2c0g5e8f3d2a4b5c6d7e8f9a0b1c2"
ACCOUNT_ID = "arjancodes"

type JSONDict = dict[str, str|int|float|bool|list|dict]

def make_request (path:str, data: JSONDict|None= None,method:str = "POST")->None:
    headers = {"Authorization": f"token {TOKEN}",
                "Accept": f"application/vnd.github.{API_VERSION_ID}+json",
                "Content-Type": "application/json"}
    full_url = f"{API_ULR}/{API_VERSION_ID}/{ACCOUNT_ID}/{path}"
    print(f"Making {method} request to {full_url}")
    print(f"Data: {data}")
    print(f"Method: {method}")
    print(f"Headers: {headers}")

def main ()-> None:
    path = "repos/arjancodes/coupling101/issues"
    data = {"title": "New issue", "body": "This is a new issue"}
    make_request(path, data, method="POST")