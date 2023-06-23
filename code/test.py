import unittest
import translator as T

class TestRengex(unittest.TestCase):

    def test_literal(self):
        regex = T.parse(["-lit", "hello"])
        self.assertEqual(regex, "hello")

    def test_literal_escape(self):
        regex = T.parse(["-lit", "dog"])
        self.assertEqual(regex, "dog")

    def test_in(self):
        regex = T.parse(["-in", "h,e,l,l,o"])
        self.assertEqual(regex, "[hello]")

    def test_range(self):
        regex = T.parse(["-in", "range:a-z"])
        self.assertEqual(regex, "[a-z]")

    def test_in_range(self):
        regex = T.parse(["-in", "a,b,range:d-f,c"])
        self.assertEqual(regex, "[abd-fc]")

    def test_group(self):
        regex = T.parse(["-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello)")

    def test_nested_group(self):
        regex = T.parse(["-(", "-lit", "hello", "-(", "-lit", "world", "-)", "-)"])
        self.assertEqual(regex, "(hello(world))")

    def test_nocapture(self):
        regex = T.parse(["-nograb(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(?:hello)")

    def test_nocapture_and_group(self):
        regex = T.parse(["-(", "-lit", "hi", "-nograb(", "-lit", "hello", "-)", "-)"])
        self.assertEqual(regex, "(hi(?:hello))")

    def test_start_end(self):
        regex = T.parse(["start", "-lit", "hello", "end"])
        self.assertEqual(regex, "^hello$")

    def test_beginning_ending(self):
        regex = T.parse(["beginning", "-lit", "hello", "ending"])
        self.assertEqual(regex, "\\Ahello\\Z")

    def test_digit(self):
        regex = T.parse(["digit"])
        self.assertEqual(regex, "\\d")

    def test_nondigit(self):
        regex = T.parse(["nondigit"])
        self.assertEqual(regex, "\\D")

    def test_letter(self):
        regex = T.parse(["letter"])
        self.assertEqual(regex, "\\w")

    def test_nonletter(self):
        regex = T.parse(["nonletter"])
        self.assertEqual(regex, "\\W")

    def test_whitespace(self):
        regex = T.parse(["whitespace"])
        self.assertEqual(regex, "\\s")

    def test_nonwhitespace(self):
        regex = T.parse(["nonwhitespace"])
        self.assertEqual(regex, "\\S")

    def test_character(self):
        regex = T.parse(["character"])
        self.assertEqual(regex, ".")

    def test_punctuation(self):
        regex = T.parse(["punctuation"])
        self.assertEqual(regex, "[:punct:]")

    def test_nocase(self):
        regex = T.parse(["-nocase", "-lit", "hello"])
        self.assertEqual(regex, "(?i)hello")

    def test_nocase_in(self):
        regex = T.parse(["-nocase", "-in", "h,e,l,l,o"])
        self.assertEqual(regex, "(?i)[hello]")
