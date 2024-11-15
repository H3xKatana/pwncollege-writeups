import requests
    ...: 
    ...: json_data = {"a": "69af1db3853ac57ceb0a9b27528f51ea"}
    ...: headers = {"Content-Type": "application/json"}
    ...: 
    ...: res = requests.post("http://localhost:80", json=json_data, headers=headers)
    ...: 
    ...: print(res.text)
