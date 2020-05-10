import unittest
from unittest.mock import Mock
import stringer


class CheckString(unittest.TestCase):
    def int_check_type_failure(self):
        message = 123
        # check failure assertion
        stringer.cut_it(message)
 