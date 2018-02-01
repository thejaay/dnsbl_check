from mxChecker import *

import socket

class TestDNS:
    def test_allDNS():
        for bl in bls:
            assert socket.gethostbyname(bl)
