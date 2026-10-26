import pytest
import requests

base_url = "https://ru.yougile.com/"

#Позитивные проверки

def test_create_project():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'

    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]
    assert my_key is not None
    
    project = {
        'title': 'new project',
        "idempotencyKey": my_key
        }

    headers = {
    "Authorization": f"Bearer {my_key}"
    }
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)

    assert resp.status_code == 201

    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)  


def test_get_project():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'
    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]
    
    project = {
        'title': 'new project',
        "idempotencyKey": my_key
            }
    
    headers = {
        "Authorization": f"Bearer {my_key}"
        }
        
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)
    
    project_id = resp.json()["id"]
    assert project_id is not None
    headers = {
                "Authorization": f"Bearer {my_key}"
                }
    resp = requests.get(base_url + 'api-v2/projects/'+ project_id, headers = headers)

    assert resp.status_code == 200

    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)


def test_edit_project():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'
    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]

    project = {
        'title': 'new project',
        'idempotencyKey': my_key
                }
        
    headers = {
        "Authorization": f"Bearer {my_key}"
            }
            
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)
        
    project_id = resp.json()["id"]
    
    project = {
            'title': 'Новый проект'
            }
    
    headers = {
        "Authorization": f"Bearer {my_key}"
        }
        
    resp = requests.put(base_url + 'api-v2/projects/'+ project_id, json=project, headers = headers)
    
    assert resp.status_code == 200

    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)


# Негативные проверик
# [POST] - проект без обязательных полей ('title')
def test_create_project_negativ():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'
    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]
    assert my_key is not None
    
    project = {
        "idempotencyKey": my_key
        }

    headers = {
    "Authorization": f"Bearer {my_key}"
}
    
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)

    assert resp.status_code == 400, (
    f"Ошибка: неверные данные в теле запроса! "
    f"Ответ сервера: {resp.text}"
)
    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)

# [GET] - •	запрос без авторизации, если она требуется

def test_get_project_negativ():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'
    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]
    
    project = {
        'title': 'new project',
        "idempotencyKey": my_key
            }
    
    headers = {
        "Authorization": f"Bearer {my_key}"
        }
        
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)
    
    project_id = resp.json()["id"]
    assert project_id is not None
    
    resp = requests.get(base_url + 'api-v2/projects/'+ project_id)

    assert resp.status_code == 401, (
        f"Ошибка! Сервер пустил пользователя без авторизации и вернул "
        f"код {resp.status_code} вместо 401. Ответ: {resp.text}"
    )

    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)

#[PUT] - обновить проект с несуществующим ID
def test_edit_project_negativ():
    creds = {
        'login': 'мой логин',
        'password': 'мой пароль'
    }
    resp = requests.post(base_url + 'api-v2/auth/companies', json=creds)
    
    company_id = resp.json()["content"][0]["id"]
        
    keys = {
        'login': 'мой логин',
        'password': 'мой пароль',
        'companyId': company_id
    }
    project_resp = requests.post(base_url + 'api-v2/auth/keys', json=keys)
    assert project_resp.status_code == 201
    
    my_key = project_resp.json()["key"]

    project = {
        'title': 'new project',
        'idempotencyKey': my_key
                }
        
    headers = {
        "Authorization": f"Bearer {my_key}"
            }
            
    resp = requests.post(base_url + 'api-v2/projects', json=project, headers = headers)
        
    project_id = resp.json()["id"]
    fake_project_id = "00000000-0000-0000-0000-000000000000"
    
    project = {
            'title': 'Новый проект'
            }
    
    headers = {
        "Authorization": f"Bearer {my_key}"
        }
        
    resp = requests.put(base_url + 'api-v2/projects/'+ fake_project_id, json=project, headers = headers)
    
    assert resp.status_code == 404, (
        f"Ожидался статус-код 404 для несуществующего проекта, "
        f"но сервер вернул {resp.status_code}. Ответ: {resp.text}"
    )

    resp = requests.delete(base_url + 'api-v2/auth/keys/' + my_key)
