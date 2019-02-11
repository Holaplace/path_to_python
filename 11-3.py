import unittest
from employee import Employee


class TestSalaryCase(unittest.TestCase):
    def setUp(self):
        self.eliot = Employee('eliot', 'xu', 10000)

    def test_give_default_raise(self):
        self.eliot.give_raise()
        self.assertEqual(self.eliot.salary, 15000)

    def test_give_custom_raise(self):
        self.eliot.give_raise(10000)
        self.assertEqual(self.eliot.salary, 20000)


unittest.main()
