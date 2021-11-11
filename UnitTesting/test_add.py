import unittest
import random
from add import *
class TestClass():
    def __init__(self) -> None:
        self.test = None

class TestAdd(unittest.TestCase):
    
# Int tests   
    def test_add_int(self):
        for i in range(1000000):
            a = random.randint(0,9223372036854775807)
            b = random.randint(0,9223372036854775807)
            self.assertEqual(add(a,b), a + b)

    def test_add_int_float(self):
        for i in range(1000000):
            a = random.randint(0,9223372036854775807)
            b = random.uniform(0,9223372036854775807)
            self.assertEqual(add(a, b), a + b)

    def test_add_int_complex(self):
        for i in range(1000000):
            a = random.randint(0,9223372036854775807)
            b = random.randint(0,9223372036854775807)
            bi = random.randint(0,9223372036854775807)
            complex_b = complex(b,bi)
            self.assertEqual(add(a,complex_b), a + complex_b)
    
    def test_add_int_class(self):
        a = random.randint(0,9223372036854775807)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(a,b)
    
    def test_add_int_string(self):
        a = random.randint(0,9223372036854775807)
        b = ''
        with self.assertRaises(TypeError):
            add(a,b)

    def test_add_int_list(self):
        a = random.randint(0,9223372036854775807)
        b = []
        with self.assertRaises(TypeError):
            add(a, b)
        
    def test_add_int_tuple(self):
        a = random.randint(0,9223372036854775807)
        b = ()
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_int_set(self):
        a = random.randint(0,9223372036854775807)
        b = {}
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_int_dict(self):
        a = random.randint(0,9223372036854775807)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(a, b)
# Int tests end

#Float tests
    def test_add_float(self):
        for i in range(1000000):
            a = random.uniform(0,9223372036854775807)
            b = random.uniform(0,9223372036854775807)
            self.assertEqual(add(a,b), a + b)

    def test_add_float_int(self):
        for i in range(1000000):
            a = random.uniform(0,9223372036854775807)
            b = random.randint(0,9223372036854775807)
            self.assertEqual(add(a, b), a + b)
    
    def test_add_float_complex(self):
        for i in range(1000000):
            a = random.uniform(0,9223372036854775807)
            b = random.randint(0,9223372036854775807)
            bi = random.randint(0,9223372036854775807)
            complex_b = complex(b, bi)
            self.assertEqual(add(a, complex_b), a + complex_b)

    def test_add_float_class(self):
        a = random.uniform(0,9223372036854775807)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_float_string(self):
        a = random.uniform(0,9223372036854775807)
        b = ""
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_float_list(self):
        a = random.uniform(0,9223372036854775807)
        b = []
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_float_tuple(self):
        a = random.uniform(0,9223372036854775807)
        b = ()
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_float_set(self):
        a = random.uniform(0,9223372036854775807)
        b = {}
        with self.assertRaises(TypeError):
            add(a, b)

    def test_add_float_dict(self):
        a = random.uniform(0,9223372036854775807)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(a, b)
#Float tests end

#Complex tests
    def test_add_complex(self):
        for i in range(1000000):
            a = random.randint(0,9223372036854775807) 
            ai = random.randint(0,9223372036854775807) 
            b = random.randint(0,9223372036854775807) 
            bi = random.randint(0,9223372036854775807) 
            complex_a = complex(a,ai)
            complex_b = complex(b,bi)
            self.assertEqual(add(complex_a,complex_b), complex_a + complex_b)

    def test_add_complex_int(self):
        for i in range(1000000):
            a = random.randint(0,9223372036854775807)
            ai = random.randint(0,9223372036854775807)
            complex_a = complex(a, ai)
            b = random.randint(0,9223372036854775807)
            self.assertEqual(add(complex_a, b), complex_a + b)
    
    def test_add_complex_float(self):
        for i in range(10000000):
            a = random.randint(0,9223372036854775807)
            ai = random.randint(0,9223372036854775807)
            complex_a = complex(a, ai)
            b = random.uniform(0,9223372036854775807)
            self.assertEqual(add(complex_a, b), complex_a + b)

    def test_add_complex_class(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(complex_a, b)
    
    def test_add_complex_string(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = ''
        with self.assertRaises(TypeError):
            add(complex_a, b)

    def test_add_complex_list(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = []
        with self.assertRaises(TypeError):
            add(complex_a, b)

    def test_add_complex_tuple(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = ()
        with self.assertRaises(TypeError):
            add(complex_a, b)
    
    def test_add_complex_set(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = {}
        with self.assertRaises(TypeError):
            add(complex_a, b)
    
    def test_add_complex_dict(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(complex_a, b)  
#Complex tests end

#Class tests
    def test_add_classes(self):
        with self.assertRaises(TypeError):
            add(TestClass(),TestClass())

    def test_add_class_int(self):
        a = random.randint(0,9223372036854775807)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(b, a)

    def test_add_class_float(self):
        a = random.uniform(0,9223372036854775807)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(b, a)

    def test_add_class_complex(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = TestClass()
        with self.assertRaises(TypeError):
            add(complex_a, b)

    def test_add_class_string(self):
        a = TestClass()
        b = ''
        with self.assertRaises(TypeError):
            add(a, b)

    def test_add_class_list(self):
        a = TestClass()
        b = []
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_class_tuple(self):
        a = TestClass()
        b = ()
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_class_set(self):
        a = TestClass()
        b = {}
        with self.assertRaises(TypeError):
            add(a, b)
    
    def test_add_class_dict(self):
        a = TestClass()
        b = {"":""}
        with self.assertRaises(TypeError):
            add(a, b)
#Class tests end

#String tests
    def test_add_string(self):
        with self.assertRaises(TypeError):
            add('','')

    def test_add_string_int(self):
        a = random.randint(0,9223372036854775807)
        b = ''
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_string_float(self):
        a = random.uniform(0,9223372036854775807)
        b = ""
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_string_complex(self):
        a = random.randint(0,92233720368547758070)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = ''
        with self.assertRaises(TypeError):
            add(b, complex_a)

    def test_add_string_class(self):
        a = TestClass()
        b = ''
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_string_collection(self):
        a = ''
        b = []
        with self.assertRaises(TypeError):
            add(a, b)
        
    def test_add_string_list(self):
        a = ''
        b = []
        with self.assertRaises(TypeError):
            add(a, b)
        
    def test_add_string_tuple(self):
        a = ''
        b = ()
        with self.assertRaises(TypeError):
            add(a, b)
        
    def test_add_string_set(self):
        a = ''
        b = {}
        with self.assertRaises(TypeError):
            add(a, b)
        
    def test_add_string_dict(self):
        a = ''
        b = {"":""}
        with self.assertRaises(TypeError):
            add(a, b)
#String tests end

#Collections tests
    def test_add_list(self):
         with self.assertRaises(TypeError):
             add([],[])
    
    def test_add_tuple(self):
         with self.assertRaises(TypeError):
             add((),())
    
    def test_add_set(self):
         with self.assertRaises(TypeError):
             add({},{})
    
    def test_add_dict(self):
         with self.assertRaises(TypeError):
             add({"":""},{"":""})

    def test_add_list_int(self):
        a = random.randint(0,9223372036854775807)
        b = []
        with self.assertRaises(TypeError):
            add(b, a)
        
    def test_add_tuple_int(self):
        a = random.randint(0,9223372036854775807)
        b = ()
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_set_int(self):
        a = random.randint(0,9223372036854775807)
        b = {}
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_dict_int(self):
        a = random.randint(0,9223372036854775807)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_list_float(self):
        a = random.uniform(0,9223372036854775807)
        b = []
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_tuple_float(self):
        a = random.uniform(0,9223372036854775807)
        b = ()
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_set_float(self):
        a = random.uniform(0,9223372036854775807)
        b = {}
        with self.assertRaises(TypeError):
            add(b, a)

    def test_add_dict_float(self):
        a = random.uniform(0,9223372036854775807)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(b, a)

    def test_add_list_complex(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = []
        with self.assertRaises(TypeError):
            add(b, complex_a)

    def test_add_tuple_complex(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = ()
        with self.assertRaises(TypeError):
            add(b, complex_a)
    
    def test_add_set_complex(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = {}
        with self.assertRaises(TypeError):
            add(b, complex_a)
    
    def test_add_dict_complex(self):
        a = random.randint(0,9223372036854775807)
        ai = random.randint(0,9223372036854775807)
        complex_a = complex(a, ai)
        b = {"":""}
        with self.assertRaises(TypeError):
            add(b, complex_a) 
    
    def test_add_list_class(self):
        a = TestClass()
        b = []
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_tuple_class(self):
        a = TestClass()
        b = ()
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_set_class(self):
        a = TestClass()
        b = {}
        with self.assertRaises(TypeError):
            add(b, a)
    
    def test_add_dict_class(self):
        a = TestClass()
        b = {"":""}
        with self.assertRaises(TypeError):
            add(b, a)

    def test_add_list_string(self):
        a = ''
        b = []
        with self.assertRaises(TypeError):
            add(b, a)
        
    def test_add_tuple_string(self):
        a = ''
        b = ()
        with self.assertRaises(TypeError):
            add(b, a)
        
    def test_add_set_string(self):
        a = ''
        b = {}
        with self.assertRaises(TypeError):
            add(b, a)
        
    def test_add_dict_string(self):
        a = ''
        b = {"":""}
        with self.assertRaises(TypeError):
            add(b, a)
#Collections tests end    

if __name__ == '__main__':
    unittest.main()