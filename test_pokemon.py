# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 06:41:35 2017

@author: krishna
"""

import unittest
from pokemon import main



class PokemonTestCase(unittest.TestCase):
    """Tests for pokemon.py`."""
    #Program passed all the test cases.Added test_complete for you to check the program
    #If you are using spyder for running this you may get certification error.It's the bug in Anaconda
    #Search for cacert.pem certificate in anaconda site-packages and paste it in certifi(C:\Users\username\Anaconda\Lib\site-packages\certifi)
    def test_complete(self):
        """Tests the main"""
        self.assertTrue(main())

if __name__ == '__main__':
    unittest.main()