class User:
    """
    Class that generates new instances of users

    """

    user_list = [] # empty password

    def __init__(self,first_name,last_name,user_name,password):

        '''
        _init_ meethod helps us to define properties for our objects

        Args:
            first_name: New user first name.
            last_name : New user last name.
            user_name: New user name.
            password : New user password.
            
        ''' 

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
