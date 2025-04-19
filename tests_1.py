# Odkodowanie payloadu
import base64, json, string,random

data = 'eyJwYXNzd29yZCI6IjctaEZrYDk7QjklPiJ9'
decoded = base64.urlsafe_b64decode(data + "==")
print(json.loads(decoded))

pass_seq = string.ascii_letters + string.digits + string.punctuation
test = ''.join(random.choice(pass_seq) for i in range(12))
print(test)