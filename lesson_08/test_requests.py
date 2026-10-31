import requests

base_url = "http://139.100.217.192:8000"

def test_simple_req():
    resp = requests.get(base_url+'/company/list')

    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "QA Студия 'ТестировщикЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"
    
def test_auth():
    creds = {
        'username': 'harrypotter',
        'password': 'expelliarmus'
    }
    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.status_code == 200
