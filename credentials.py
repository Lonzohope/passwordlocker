class Credentials:

    '''
    Class that generates new instances of credentials

    '''

    credentials_list = [] # empty password


    def __init__(self,first_name,last_name,user_name,password,platform):

            '''
            _init_ method helps us to define properties for our objects

            Args:
                first_name: New  first name.
                last_name : New  last name.
                user_name: New user name.
                password : New password.
                platform: New platform
            ''' 


            self.first_name = first_name
            self.last_name = last_name
            self.user_name = user_name
            self.password = password
            self.platform = platform

    credentials_list = [] # Empty credentials list
    # Init method up here
    def save_credentials(self):

            '''
            save_credentials method saves credentials objects into credentials_list
            '''

            Credentials.credentials_list.append(self)

    def delete_credentials(self):

            '''
            delete_credentials method deletes a saved credentials from the credentials_list
            '''

            Credentials.credentials_list.remove(self)


@classmethod
    def find_by_username(cls,username):
            '''
            Method that takes in username and returns a credentials that matches that username.

            Args:
                username:  to search for
            Returns :
                Credentials of person that matches the username.
            '''

        for credentials in cls.credentials_list:
            if credentials.user_name== name:
                return credentials
