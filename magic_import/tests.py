import os
import unittest
from magic_import import get_caller_globals
from magic_import import get_caller_locals
from magic_import import import_module
from magic_import import import_from_string


g01 = "hello"

class TestMagicImport(unittest.TestCase):

    def test01(self):
        def hello():
            return get_caller_locals()
        a01 = 12341
        ls = hello()
        print(ls)
        print(ls.keys())
        b01 = ls["a01"]
        assert a01 == b01

    def test02(self):
        def hello():
            return get_caller_globals()
        gs = hello()
        print(gs)
        print(gs.keys)
        b01 = gs["g01"]
        assert b01 == g01

    def test03(self):
        os = import_module("os")
        assert hasattr(os, "listdir")

    def test04(self):
        os = import_module("not-exist-module")
        assert os is None

    def test05(self):
        os = import_from_string("os")
        assert hasattr(os, "listdir")

    def test06(self):
        listdir = import_from_string("os.listdir")
        assert callable(listdir)

    def test07(self):
        class C(object):
            value = 3
        c = C()
        data = {
            "a": {
                "b": {
                    "c": c
                }
            }
        }
        v = import_from_string("data.a.b.c.value")
        assert v == 3

    def test08(self):
        none = import_from_string("not-exist-module")
        assert none is None

    def test09(self):
        t09 = "hello"
        v09 = import_from_string("t09")
        assert v09 == t09

    def test10(self):
        class C(object):
            value = 10
        c = C()
        assert import_from_string("c.value") == 10

    def test11(self):
        if os.sys.version.startswith("2.6"):
            self.assertRaises(ImportError, lambda:import_from_string("not-exist-module", slient=False))
        else:
            with self.assertRaises(ImportError):
                import_from_string("not-exist-module", slient=False)

    def test12(self):
        t12 = [1,2]
        none = import_from_string("t12.2")
        assert none is None
