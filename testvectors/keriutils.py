from json import dumps as json_dumps
from base64 import urlsafe_b64encode as b64encode

from blake3 import blake3

KERI_VERSION_FMT = 'KERI10JSON%06x_'

def json_dumps_compact(v):
    return json_dumps(v, separators=(',', ':'))

def json_dumps_pretty(v):
    return json_dumps(v, indent=4)

class CESR:
    @staticmethod
    def digest_blake3(v):
        b = v.encode('utf-8')
        digest = blake3(b).digest()
        assert len(digest) == 32

        b64 = b64encode(b'\x00' + digest)
        assert len(b64) == 44

        qb64 = b'E' + b64[1:]
        return qb64.decode('utf-8')
