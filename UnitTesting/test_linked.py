import random
import unittest
from doubleLinked import DoubleLinkedList

class TestList(unittest.TestCase):

    def test_search(self):
        dlinked_list = DoubleLinkedList()
        for i in range(1000000):
            dlinked_list.insert_last(random.randint(1,1000))
        # dlinked_list.count_same_values(186)
    
    # def test_assert_in(self):
    #     dlinked_list = DoubleLinkedList()
    #     dlinked_list.insert_last(1)
    #     self.assertIn(1, dlinked_list)
    
    # def test_assert_not_in(self):
    #     dlinked_list = DoubleLinkedList()
    #     dlinked_list.insert_last(1)
    #     self.assertNotIn(0, dlinked_list)
        
if __name__ == '__main__':
    unittest.main()