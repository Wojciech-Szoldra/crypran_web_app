import base64, json, datetime

data = 'eyJwYXNzd29yZCI6IjctaEZrYDk7QjklPiJ9'
decoded = base64.urlsafe_b64decode(data + "==")
print(json.loads(decoded))


# Twój segment timestampu
ts_b64 = 'aAPIUw'

# 1) Dodaj padding i zdekoduj do bajtów
b = base64.urlsafe_b64decode(ts_b64 + '==')

# 2) Zamień bajty na liczbę (big‑endian)
timestamp = int.from_bytes(b, 'big')

# 3) (Opcjonalnie) Konwersja na czytelny czas
dt = datetime.datetime.utcfromtimestamp(timestamp)

print("Unix timestamp:", timestamp)
print("UTC datetime:   ", dt)