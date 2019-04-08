import unittest # Importing the unittest module from user import User # Importing the user class
from user import User
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''

    #Items up here ....

    def setUp(self):
        '''

        Set up method to run before each test cases.
        '''

        self.new_user = User("Hope","Kilonzo","lonzo","MIT") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Hope")
        self.assertEqual(self.new_user.last_name,"Kilonzo")
        self.assertEqual(self.new_user.user_name,"lonzo")
        self.assertEqual(self.new_user.password,"MIT")


if __name__== '__main__':
    unittest.main()