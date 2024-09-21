import unittest
from muliply import multiplication
class multiplyTestCase(unittest.TestCase):

  def test_1(self):

    result =multiplication(3,4)
    self.assertEqual(result,12)

 def test_2(self):

   result =multiplication(3,-4)
   self.assertEqual(result,-12)
 def test_3(self):

   result =multiplication(-3,4)
   self.assertEqual(result,-12) 
 def test_4(self):

   result =multiplication(-3,-4)
   self.assertEqual(result,12)
if __name__ ='__main__':
  unittest.main()

