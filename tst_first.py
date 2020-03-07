import unittest
import main

class MyTestCase(unittest.TestCase):
    def tst_main(self):
        self.assertEqual(main.main(), True)

if __name__ == '__main__':
    unittest.main()
