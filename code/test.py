import unittest
import translator as T

# Class to test rENGex!
class TestRengex(unittest.TestCase):

# Test literal flag and chaaracter escapting.
    def test_literal(self):
        regex = T.parse(["-lit", "hello"])
        self.assertEqual(regex, "hello")

    # Because the regex needs the escape and we need the escape, \\\\ represents one backslash in the regex.
    def test_literal_escape(self):
        regex = T.parse(["-lit", "dog\\"])
        self.assertEqual(regex, "dog\\\\")

# Test in and range functions
    def test_in(self):
        regex = T.parse(["-in", "h,e,l,l,o"])
        self.assertEqual(regex, "[hello]")

    def test_range(self):
        regex = T.parse(["-in", "range:a-z"])
        self.assertEqual(regex, "[a-z]")

    def test_in_range(self):
        regex = T.parse(["-in", "a,b,range:d-f,c"])
        self.assertEqual(regex, "[abd-fc]")


# Test groups and no capture groups.
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


# Nocase flag tests.
    def test_nocase(self):
        regex = T.parse(["-nocase", "-lit", "hello"])
        self.assertEqual(regex, "(?i)hello")

    def test_nocase_in(self):
        regex = T.parse(["-nocase", "-in", "h,e,l,l,o"])
        self.assertEqual(regex, "(?i)[hello]")


# Groupref tests
    def test_groupref(self):
        regex = T.parse(["-(", "-lit", "hello", "-)", "-groupref", "1"])
        self.assertEqual(regex, "(hello)\\1")

    def test_zero_groupref_exception(self):
        regex = lambda: T.parse(["-(", "-lit", "hello", "-)", "-groupref", "-1"])
        self.assertRaises(Exception, regex)

    def test_negative_groupref_exception(self):
        regex = lambda: T.parse(["-(", "-lit", "hello", "-)", "-groupref", "-1"])
        self.assertRaises(Exception, regex)


# Quantifier tests
    def test_quantifier_0_plus(self):
        regex = T.parse(["0+", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello)*")

    def test_quantifier_1_plus(self):
        regex = T.parse(["1+", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello)+")

    def test_quantifier_2_plus(self):
        regex = T.parse(["2+", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello){2,}")

    def test_quantifier_single_number(self):
        regex = T.parse(["5", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello){5}")

    def test_quantifier_double_digit(self):
        regex = T.parse(["12", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello){12}")

    def test_quantifier_range(self):
        regex = T.parse(["5-12", "-(", "-lit", "hello", "-)"])
        self.assertEqual(regex, "(hello){5,12}")

    def test_quantifier_invalid_range_exception(self):
        regex = lambda: T.parse(["12-5", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_quantifier_negative_range_exception(self):
        regex = lambda: T.parse(["-5", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_invalid_plus_exception(self):
        regex = lambda: T.parse(["+", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_too_early_plus_exception(self):
        regex = lambda: T.parse(["+5", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_too_many_plus_exception(self):
        regex = lambda: T.parse(["5++", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_plus_and_desh_exception(self):
        regex = lambda: T.parse(["5+-", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_invalid_dash_exception(self):
        regex = lambda: T.parse(["-", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_too_early_dash_exception(self):
        regex = lambda: T.parse(["-5", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)


# Test for parse exceptions
    def test_invalid_token_exception(self):
        regex = lambda: T.parse(["-invalid", "-(", "-lit", "hello", "-)"])
        self.assertRaises(Exception, regex)

    def test_invalid_token_exception_2(self):
        regex = lambda: T.parse(["-(", "-lit", "hello", "-)", "invalid"])
        self.assertRaises(Exception, regex)

# Test substitutions
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

    def test_wordedge(self):
        regex = T.parse(["wordedge"])
        self.assertEqual(regex, "\\b")

    def test_nonwordedge(self):
        regex = T.parse(["nonwordedge"])
        self.assertEqual(regex, "\\B")

    def test_character(self):
        regex = T.parse(["character"])
        self.assertEqual(regex, ".")

    def test_punctuation(self):
        regex = T.parse(["punctuation"])
        self.assertEqual(regex, "[:punct:]")
