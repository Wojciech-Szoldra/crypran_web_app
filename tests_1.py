# Odkodowanie payloadu
import base64, json

data = 'eJwNyMENgCAMBdBdmKDYAr8uY5oWw00jBw_G3fX43pNOm_M-rtiGzZHW5HnvC0er6lQA91JZzfBHjjAKzQQVFzDArCql_1YSmINaej8-9ReW'
decoded = base64.urlsafe_b64decode(data + "==")
print(json.loads(decoded))