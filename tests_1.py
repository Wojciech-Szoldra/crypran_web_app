# Odkodowanie payloadu
import base64, json, string, random, hashlib

data = 'eyJwYXNzd29yZCI6IjctaEZrYDk7QjklPiJ9'
decoded = base64.urlsafe_b64decode(data + "==")
print(json.loads(decoded))

def generate_password():
    pass_seq = string.ascii_letters + string.digits + string.punctuation
    return''.join(random.choice(pass_seq) for i in range(10))

# SHA256 test
def hash_test(test_string):
    return hashlib.sha256(test_string.encode()).hexdigest()

hash1 = hash_test('test1')
hash2 = hash_test('test1')

if hash1 == hash2:
    print(f'hash1: {hash1} \nhash2: {hash2} \nHashes are equal')