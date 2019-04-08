import unittest # Importing the unittest module from credentials import Credentials # Importing the user class
from credentials import Credentials

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

                self.new_credentials = Credentials("Hope","Kilonzo","lonzo","MIT","twitter") # create credentials object


        def test_init(self):
                '''
                test_init test case to test if the object is initialized properly
                '''

                self.assertEqual(self.new_credentials.first_name,"Hope")
                self.assertEqual(self.new_credentials.last_name,"Kilonzo")
                self.assertEqual(self.new_credentials.user_name,"lonzo")
                self.assertEqual(self.new_credentials.password,"MIT")
                self.assertEqual(self.new_credentials.platform,"twitter")


        def test_save_credential(self):
                '''
                test_save_username test case to test if the credentials object is saved into the credntials list

                test_save_password test case to test if the credentials object is saved into the credentials list
                
                test_save_platform test case to test if the credentials object is saved into the credentials list       
                
                '''

                self.new_username.save_username() # saving the new username
                self.new_password.save_password() # saving the new password
                self.new_platform.save_platform() # saving the new platform
                self.assertEqual(len(User.user_list),1)


        # Items up here...

        def test_save_multiple_credentials(self):
                '''
                test_save_multiple_credentials to check if we can save multiple credentials
                objects to our credentials_list
                '''
                self.new_credentials.save_credentials()
                test_credentials = Credentials("Test","user","meme","password","instagram") # new contact
                test_credentials.save_credentials()
                self.assertEqual(len(Credentials.credentials_list),2)


# More tests above
       
        def test_delete_credentials(self):

                '''
        
                test_delete_credentials to test if we can remove a credentials from our credentials list
                '''
                self.new_credentials.save_credentials()
                test_credentials = Credentials("Test","user","meme","password","instagram") # new contact
                test_credentials.save_credentials()

                self.new_credentials.delete_credentials()# Deleting a credentials object
                self.assertEqual(len(Credentials.credentials_list),1)


        
if __name__== '__main__':
     unittest.main()