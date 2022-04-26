# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaLib.Fixes import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Fixes_Asyncio(unittest.TestCase):
    def test_nested_asyncio(self):
        try:
            fix_nested_asyncio()
        except ImportError:
            self.fail("test_nested_asyncio couldn't import the nessary module to fix the issue")