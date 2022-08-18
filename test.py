#! /usr/bin/env python

import unittest, hashlib
from sha256 import sha256


class Testing(unittest.TestCase):
    def test_utf8_input(self):
        input = ""
        for _ in range(128):
            algo = hashlib.sha256()
            algo.update(bytes(input, "utf8"))
            self.assertEqual(sha256(input), algo.hexdigest())
            input += "a"

    def test_hex_input(self):
        input = "aa"
        for _ in range(128):
            algo = hashlib.sha256()
            algo.update(bytes.fromhex(input))
            self.assertEqual(sha256(input, True), algo.hexdigest())
            input += "aa"

    def test_invalid_hex_input(self):
        input = "xxx"
        with self.assertRaisesRegex(ValueError, f"Invalid hex input: {input}"):
            sha256(input, True)

        input = "aee"
        with self.assertRaisesRegex(ValueError, f"Invalid hex input: {input}"):
            sha256(input, True)

if __name__ == '__main__':
    unittest.main()