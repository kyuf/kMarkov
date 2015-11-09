import unittest
from markov_generator import *
import os

class TestTextData(unittest.TestCase):
    
    def test_prefix(self):
        test = TextData(['I', 'like', 'to', 'run'], 2)
        #test dictionary construction
        test_set = set()
        for key in test.get_prefix_dict():
            test_set.add(key)
        self.assertEqual(test_set, {'I like', 'like to'})
        #test random prefix selection
        self.assertTrue(test.get_prefix() in test.get_prefix_dict())
        #test update prefix
        test.set_prefix('I like')
        test.set_suffix('to')
        test.update_prefix()
        self.assertEqual(test.get_prefix(), 'like to')

if __name__ == '__main__':
    os.system('clear')
    unittest.main(verbosity=2)
