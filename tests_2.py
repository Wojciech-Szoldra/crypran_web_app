import hmac, hashlib

secret_key = b"moj_tajny_klucz"
message    = b"Dane do uwierzytelnienia"

h = hmac.new(secret_key, message, hashlib.sha256)
print("HMAC-SHA256:", h.hexdigest())