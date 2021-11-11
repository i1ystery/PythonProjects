import random
import math
import unittest
from lhv import *
class TestLahev(unittest.TestCase):

    def test_set_capacity(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, 9223372036854775807)
            lhv.set_capacity(rng_capacity)
            self.assertTrue(lhv.capacity == rng_capacity)

    def test_set_amount(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, 9223372036854775807)
            rng_amount = random.randint(0, rng_capacity)
            lhv.set_capacity(rng_capacity)
            lhv.set_amount(rng_amount)
            self.assertTrue(lhv.amount == rng_amount)

    def test_clr_amount(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, 9223372036854775807)
            rng_amount = random.randint(0, rng_capacity)
            lhv.set_capacity(rng_capacity)
            lhv.set_amount(rng_amount)
            lhv.clr_amount()
            self.assertTrue(lhv.amount == 0)

    def test_set_amount_ml(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, math.floor(9223372036854775807 / 1000))
            rng_amount = random.randint(0, rng_capacity * 1000)
            lhv.set_capacity(rng_capacity)
            lhv.set_amount_ml(rng_amount)
            self.assertTrue(lhv.amount == rng_amount / 1000)

    def test_get_amount_ml(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, math.floor(9223372036854775807 / 1000))
            rng_amount = random.randint(0, rng_capacity)
            lhv.set_capacity(rng_capacity)
            lhv.set_amount(rng_amount)
            self.assertEqual(lhv.get_amount_ml(), rng_amount * 1000)

    def test_open(self):
        lhv = Lahev()
        lhv.close()
        self.assertTrue(lhv.is_closed)

    def test_close(self):
        lhv = Lahev()
        lhv.is_closed = True
        lhv.open()
        self.assertFalse(lhv.is_closed)

    def test_fill_negative_amount(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, 9223372036854775807)
            rng_amount = random.randint(0, rng_capacity) * - 1
            lhv.set_capacity(rng_capacity)
            with self.assertRaises(FillException):
                lhv.set_amount(rng_amount)
    
    def test_fill_negative_amount_in_ml(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0, math.floor(9223372036854775807 / 1000))
            rng_amount = random.randint(0, rng_capacity * 1000) * - 1
            lhv.set_capacity(rng_capacity)
            with self.assertRaises(FillException):
                lhv.set_amount_ml(rng_amount)

    def test_fill_more_than_capacity(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0,9223372036854775807)
            rng_amount = random.randint(rng_capacity + 1, 9223372036854775807)
            lhv.set_capacity(rng_capacity)
            with self.assertRaises(FillException):
                lhv.set_amount(rng_amount)

    def test_set_negative_capacity(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0,9223372036854775807) * - 1
            with self.assertRaises(CapacityException):
                lhv.set_capacity(rng_capacity)
    
    def test_set_zero_capacity(self):
        lhv = Lahev()
        with self.assertRaises(CapacityException):
            lhv.set_capacity(0)

    def test_empty_while_closed(self):
        lhv = Lahev()
        lhv.close()
        with self.assertRaises(BottleClosedException):
            lhv.clr_amount()

    def test_fill_while_closed(self):
        for i in range(1000000):
            lhv = Lahev()
            rng_capacity = random.randint(0,9223372036854775807)
            rng_amount = random.randint(0, rng_capacity)
            lhv.set_capacity(rng_capacity)
            lhv.close()
            with self.assertRaises(BottleClosedException):
                lhv.set_amount(rng_amount)


if __name__ == '__main__':
    unittest.main()