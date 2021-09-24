import hashlib


def hash_string(string):
    hash_object = hashlib.sha256(string.encode('utf-8'))
    return hash_object.hexdigest()
