import unittest
import translator as T

class TestRengex(unittest.TestCase):

    def test_literal(self):
        regex = T.parse(["-lit", "hello"])
        self.assertEqual(regex, "hello")

    def test_literal_escape(self):
        regex = T.parse(["-lit", ""])