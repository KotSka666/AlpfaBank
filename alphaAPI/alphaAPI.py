import requests

# Данные для подключения
client_id = "982afbb8-64b7-467d-bb84-80000daf9b4c"
redirect_uri = "http://localhost"
scope = "transactions"
api_key = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
token_url = "https://sandbox.alfabank.ru/api/v1/endpoint"
transactions_url = "https://partner.alfabank.ru/public-api/v2/transactions"

# Укажите путь к преобразованному файлу .pem
cert_path = "cert_and_key.pem"

def get_access_token():
    auth_data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "code": "AUTHORIZATION_CODE",  # Вставьте ваш authorization code
    }
    try:
        response = requests.post(token_url, data=auth_data, cert=cert_path, verify=False)
        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            print("Ошибка получения токена:", response.json())
            return None
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения:", e)
        return None

def get_transactions(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "API-key": api_key,
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(transactions_url, headers=headers, cert=cert_path, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            print("Ошибка получения выписки:", response.json())
            return None
    except requests.exceptions.RequestException as e:
        print("Ошибка подключения:", e)
        return None

def main():
    access_token = get_access_token()
    if access_token:
        transactions = get_transactions(access_token)
        if transactions:
            print("Выписка по счету:")
            print(transactions)

if __name__ == "__main__":
    main()
