import jwt
import time


def make_token(data):
    key = "DD3CDFABD79E9723457679FCA39BF9A433A439AA525EF6FCB8476156F7A929E9"
    now = time.time()
    expiretime = 60 * 60
    payload = {
        "username": data.username,
        "expire": now + expiretime
    }
    return jwt.encode(payload, key, algorithm='HS256')
