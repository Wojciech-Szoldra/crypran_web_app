import base64
import json
import zlib

# Payload z ciasteczka sesyjnego (bez początkowej kropki)
payload = "eJwNyMENgCAMBdBdmKDYAr8uY5oWw00jBw_G3fX43pNOm_M-rtiGzZHW5HnvC0er6lQA91JZzfBHjjAKzQQVFzDArCql_1YSmINaej8-9ReW"

# Dekodowanie z Base64
padded_payload = payload + "=" * (-len(payload) % 4)  # Dodanie paddingu
decoded_data = base64.urlsafe_b64decode(padded_payload)

try:
    # Próba dekompresji danych
    decompressed_data = zlib.decompress(decoded_data)
    # Dekodowanie JSON
    json_data = json.loads(decompressed_data)
    print("Odkodowane dane sesji:", json_data)
    
    # Sprawdzanie, czy hasło jest dostępne
    if 'password' in json_data:
        print(f"Znaleziono hasło: {json_data['password']}")
    elif 'password_hash' in json_data:
        print(f"Znaleziono hash hasła: {json_data['password_hash']}")
    else:
        print("Nie znaleziono hasła ani jego hasha w danych sesji")
except Exception as e:
    print(f"Błąd podczas przetwarzania: {e}")