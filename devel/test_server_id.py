#!/usr/bin/env python
import unittest
from test import TestHelper, Conn, parse

class TestForward(TestHelper):
    def test_no_server_id(self):
        resp = Conn().get("/", method = 'BOGUS')
        status, hdrs, body = parse(resp)
        self.assertContains(status, "400 Bad Request")
        self.assertFalse(hdrs.has_key("Server"))
        self.assertFalse("Generated by darkhttpd/" in body)

if __name__ == '__main__':
    unittest.main()

# vim:set ts=4 sw=4 et:
