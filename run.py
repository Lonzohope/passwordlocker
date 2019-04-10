#!/usr/bin/env python3.6

from credentials import Credentials

def create_credentials(fname,lname,uname,password,platform):
    '''
    Function to create a new credentials
    '''
    new_credentilas = Credentials(fname,lname,uname, password,platform)
    return new_credentilas


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()
  

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a credentials by name and returns the credentials
    '''
    return Credentials.find_by_name(name)

def check_existing_credentials(name):
    '''
    Function that check if a credentials exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def main():
    print("Hello Welcome to your credentials list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentilas, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("User name ...")
            u_name = input()

            print("password ...")
            password = input()

            print("platform ...")
            platform = input()



            save_credentials(create_credentials(f_name,l_name,u_name,password,platform)) # create and save new credentials.
            print ('\n')
            print(f"New Credentials {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

                if display_credentials():
                    print("Here is a list of all your credentials")
                    print('\n')

                    for credentials in display_credentials():
                        print(f"{credentials.first_name} {credentials.last_name} .....{credentials.user_name}")

                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any credentials saved yet")
                    print('\n')

        elif short_code == 'fc':

            print("Enter the name you want to search for")

            search_name = input()
            if check_existing_credentials(search_name):
                    search_credentials = find_credentials(search_name)
            print(f"{search_credentials.first_name} {search_credentials.last_name}")
            print('-' * 20)

            print(f"User name.......{search_credentials.user_name}")
            print(f"platform.......{search_crdentials.platform}")
                

        elif short_code == "ex":
            print("Bye .......")
            print('\n')
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()