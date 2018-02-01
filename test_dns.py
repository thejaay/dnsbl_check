from mxChecker import *

class TestDNS:
    def test_allDNS():
        for bl in bls:
            assert socket.gethostbyname(bl)
