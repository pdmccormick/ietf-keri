from keriutils import *

class BaseTestVector:
    pass


class TestVector_ICP_NonSelf_Blake3_1(BaseTestVector):
    NAME    = 'icp-nonself-blake3-1'

    EXPECT  = r'''{"v":"KERI10JSON0000fd_","t":"icp","d":"EK-a48AkgHnSvvBa4kBPpRwDTAeDXtrz1icsBVFwsLor","i":"BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR","s":"0","kt":"1","k":["BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR"],"nt":"0","n":[],"bt":"0","b":[],"c":[],"a":[]}'''

    EVENT = {
            'v': 'KERI10JSON......_',
            't': 'icp',
            'd': '............................................', # 32 characters
            'i': 'BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR',
            's': '0',
            'kt': '1',
            'k': [ 'BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR' ],
            'nt': '0',
            'n': [],
            'bt': '0',
            'b': [],
            'c': [],
            'a': [],
            }

    def generate(self):
        e = self.EVENT.copy()

        # Fill Event SAID digest field with dummy placeholder characters
        e['d'] = '#' * len(e['d'])

        # 1st encode to determine final length
        n = len(json_dumps_compact(e))
        e['v'] = KERI_VERSION_FMT % n

        # 2nd encode with dummy placeholder and final length to calculate digest
        e['d'] = CESR.digest_blake3(json_dumps_compact(e))

        # Ready for 3rd and final encode
        return e


class TestVector_ICP_Self_Blake3_1(BaseTestVector):
    NAME    = 'icp-self-blake3-1'

    EXPECT  = r'''{"v":"KERI10JSON0000fd_","t":"icp","d":"EH8k3e7WDowe-ed7LSedT96BulO496P3g74uPlWBKqJr","i":"EH8k3e7WDowe-ed7LSedT96BulO496P3g74uPlWBKqJr","s":"0","kt":"1","k":["BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR"],"nt":"0","n":[],"bt":"0","b":[],"c":[],"a":[]}'''

    EVENT = {
            'v': 'KERI10JSON......_',
            't': 'icp',
            'd': '............................................', # 32 characters
            'i': '............................................', # 32 characters
            's': '0',
            'kt': '1',
            'k': [ 'BN5Lu0RqptmJC-iXEldMMrlEew7Q01te2fLgqlbqW9zR' ],
            'nt': '0',
            'n': [],
            'bt': '0',
            'b': [],
            'c': [],
            'a': [],
            }

    def generate(self):
        e = self.EVENT.copy()

        # Fill Identifier Prefix and Event SAID digest fields with dummy placeholder characters
        e['i'] = '#' * len(e['i'])
        e['d'] = '#' * len(e['d'])

        # 1st encode to determine final length
        n = len(json_dumps_compact(e))
        e['v'] = KERI_VERSION_FMT % n

        # 2nd encode with dummy placeholder and final length to calculate digest
        aid = CESR.digest_blake3(json_dumps_compact(e))
        e['i'] = aid
        e['d'] = aid

        # Ready for 3rd and final encode
        return e


class TestVector_ICP_Self_Blake3_2(BaseTestVector):
    NAME    = 'icp-self-blake3-2'

    EXPECT  = r'''{"v":"KERI10JSON0002d4_","t":"icp","d":"EJ9iBRWJ_rjNMQf7tlhkYmLolWi57nlGtpnn71wCdaG9","i":"EJ9iBRWJ_rjNMQf7tlhkYmLolWi57nlGtpnn71wCdaG9","s":"0","kt":"2","k":["DnmwyZ-i0H3ULvad8JZAoTNZaU6JR2YAfSVPzh5CMzS6b","DZaU6JR2nmwyZ-VPzhzSslkie8c8TNZaU6J6bVPzhzS6b","Dd8JZAoTNnmwyZ-i0H3U3ZaU6JR2LvYAfSVPzhzS6b5CM"],"nt":"3","n":["ETNZH3ULvYawyZ-i0d8JZU6JR2nmAoAfSVPzhzS6b5CM","EYAfSVPzhzaU6JR2nmoTNZH3ULvwyZb6b5CMi0d8JZAS","EnmwyZdi0d8JZAoTNZYAfSVPzhzaU6JR2H3ULvS6b5CM","ETNZH3ULvS6bYAfSVPzhzaU6JR2nmwyZfi0d8JZ5s8bk","EJR2nmwyZ2i0dzaU6ULvS6b5CM8JZAoTNZH3YAfSVPzh"],"bt":"2","b":["BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo","BuyRFMideczFZoapylLIyCjSdhtqVb31wZkRKvPfNqkw","Bgoq68HCmYNUDgOz4Skvlu306o_NY-NrYuKAVhk3Zh9c"],"c":[],"a":[]}'''

    EVENT = {
            'v': 'KERI10JSON......_',
            't': 'icp',
            'd': '............................................', # 32 characters
            'i': '............................................', # 32 characters
            's': '0',
            'kt': '2',
            'k': [
                'DnmwyZ-i0H3ULvad8JZAoTNZaU6JR2YAfSVPzh5CMzS6b',
                'DZaU6JR2nmwyZ-VPzhzSslkie8c8TNZaU6J6bVPzhzS6b',
                'Dd8JZAoTNnmwyZ-i0H3U3ZaU6JR2LvYAfSVPzhzS6b5CM',
                ],
            'nt': '3',
            'n': [
                'ETNZH3ULvYawyZ-i0d8JZU6JR2nmAoAfSVPzhzS6b5CM',
                'EYAfSVPzhzaU6JR2nmoTNZH3ULvwyZb6b5CMi0d8JZAS',
                'EnmwyZdi0d8JZAoTNZYAfSVPzhzaU6JR2H3ULvS6b5CM',
                'ETNZH3ULvS6bYAfSVPzhzaU6JR2nmwyZfi0d8JZ5s8bk',
                'EJR2nmwyZ2i0dzaU6ULvS6b5CM8JZAoTNZH3YAfSVPzh',
                ],
            'bt': '2',
            'b': [
                'BGKVzj4ve0VSd8z_AmvhLg4lqcC_9WYX90k03q-R_Ydo',
                'BuyRFMideczFZoapylLIyCjSdhtqVb31wZkRKvPfNqkw',
                'Bgoq68HCmYNUDgOz4Skvlu306o_NY-NrYuKAVhk3Zh9c',
                ],
            'c': [],
            'a': [],
            }

    def generate(self):
        e = self.EVENT.copy()

        # Fill Identifier Prefix and Event SAID digest fields with dummy placeholder characters
        e['i'] = '#' * len(e['i'])
        e['d'] = '#' * len(e['d'])

        # 1st encode to determine final length
        n = len(json_dumps_compact(e))
        e['v'] = KERI_VERSION_FMT % n

        # 2nd encode with dummy placeholder and final length to calculate digest
        aid = CESR.digest_blake3(json_dumps_compact(e))
        e['i'] = aid
        e['d'] = aid

        # Ready for 3rd and final encode
        return e


TESTVECTORS = [
        TestVector_ICP_NonSelf_Blake3_1,
        TestVector_ICP_Self_Blake3_1,
        TestVector_ICP_Self_Blake3_2,
        ]
