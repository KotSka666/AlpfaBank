import requests

url = "https://baas.alfabank.ru/oidc/clients/:clientId/client-secret"

payload={}
headers = {
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)