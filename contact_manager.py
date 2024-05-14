# Comprehensive practice problems for week 1

# Contact Manager
# Create a small application using functions that allows adding, removing, and searching for contacts in
# a dictionary. The contacts should be stored as a dictionary of names and phone numbers. 
# Save the results to a file when the user chooses to end the program. Also incorporate reading in the file.


# Error-Handled File Processor
# Enhance the Contact Manager by adding robust error-handling to manage situations like incorrect user inputs,
# attempts to remove contacts that don't exist, and handles file errors when reading/writing.

import sys


def greeting():
    '''
    Greets the user and asks for the file to be opened. 
    Parameters: 
    - None
    
    Returns:
    - user_inp (str): The path of the file to be opened.
    '''
    
    print("Hello! Welcome to the contact manager!")
    user_inp = input("Please enter the path to the file you would like to use:")
    return user_inp

    
def open_file(file_path):
    '''
    Attempts to open and read file that contains the contact information. 
    
    Parameters:
    - file_path (str): The path of the file to be opened.

    Returns:
    - dict: A dictionary containing the contact information if the file exists and is readable. 
      Returns an empty dictionary if the file does not exist and is created anew.

    Raises:
    - SystemExit: Exits the program with a status code of 0 if the user chooses not to create a non-existent file, 
      or with a status code of 1 if a permission error or an I/O error occurs.

    The function handles FileNotFoundError to check if the file exists and prompts the user to either create a new file or exit.
    PermissionError and IOError are handled to manage permissions issues or other I/O problems.
    '''
    data = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split(':')
                data[key] = value
        return data
    except FileNotFoundError:
        new_file = input(f'{file_path} does not exist. Would you like to create this file? (y/n): ')
        if new_file.lower() == 'y':
            print("Creating new file.")
            with open(file_path, 'w') as f:
                f.write("")
            return data
        else:
            print("Exiting program as per user request.")
            sys.exit(0)  # Exit cleanly with exit code 0
    except PermissionError:
        print("Permission denied: You do not have the rights to access the file.")
        sys.exit(1)  # Exit with error code because of a permissions issue
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        sys.exit(1)  # Exit with error code because of an I/O issue

def display_all(data):
    '''
    Displays all the entries in the contact dictionary.
    
    Parameters:
    - data (dict): The dictionary where contact names are keys and phone numbers are values.
    
    Returns:
    - None: This function does not return anything as it is meant to print the contacts directly to the console.
    
    Raises:
    - None: This function does not raise any exceptions under normal circumstances.
    
    Example:
    >>> display_all({'Alice':'123-456-7890', 'Bob':'234-567-8901'})
    Alice: 123-456-7890
    Bob: 234-567-8901
    '''
    for key in data:
        print(f"{key}: {data[key]}")
        
def add_contact(data):
    '''
    Prompts the user to add a new contact name and phone number to the provided dictionary. 
    If the contact name already exists, the user can choose to overwrite it. The function 
    ensures that neither the contact name nor the phone number is empty. If the user tries 
    to exit via Ctrl+C or an unexpected input end occurs, the function exits the program.
    
    Parameters:
    - data (dict): The dictionary where contact names are keys and phone numbers are values.
    
    Returns:
    - None: This function modifies the 'data' dictionary in place and does not return anything.
    
    Raises:
    - KeyboardInterrupt: Exits the program if the user interrupts the execution (e.g., by pressing Ctrl+C).
    - EOFError: Exits the program if an unexpected end of input is encountered.

    Usage Example:
    >>> contacts = {}
    >>> add_contact(contacts)
    Who would you like to add? Alice
    What is their phone number? 123-456-7890
    New contact added: Alice: 123-456-7890
    '''
    while True:
        try:
            new_name = input("Who would you like to add? ").strip()
            if not new_name:
                print("The contact name cannot be empty. Please try again.")
                continue
            
            if new_name in data:
                overwrite = input(f"{new_name} already exists. Do you want to overwrite their number? (y/n): ").strip().lower()
                if overwrite != 'y':
                    print("Operation canceled. No new contact was added. Returning to main menu. ")
                    return
                
            new_number = input("What is their phone number? ").strip()
            if not new_number:
                print("The phone number cannot be empty. Please try again. ")
                continue
            data[new_name] = new_number
            print(f'New contact added: {new_name}: {data[new_name]}')
            return
        
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting...")
            sys.exit(1)
        except EOFError:
            print("\nUnexpected end of input. Exiting...")
            sys.exit(1)
        


def delete_contact(data):
    '''
    Prompts the user to delete an existing contact name and phone number from the provided dictionary. 
    The user is asked to confirm deletion. The function ensures that the contact name is not empty. 
    If the name does not exist, the function returns to the main menu. If the user tries 
    to exit via Ctrl+C or an unexpected input end occurs, the function exits the program.

    Parameters:
    - data (dict): The dictionary where contact names are keys and phone numbers are values.
    
    Returns:
    - None: This function modifies the 'data' dictionary in place and does not return anything.
    
    Raises:
    - KeyboardInterrupt: Exits the program if the user interrupts the execution (e.g., by pressing Ctrl+C).
    - EOFError: Exits the program if an unexpected end of input is encountered.

    Usage Example:
    >>> contacts = {'Alice':'123-456-7890'}
    >>> delete_contact(contacts)
    Who's contact would you like to delete? Alice
    Are you sure you want to delete the contact for Alice? (y/n): y
    Contact information for Alice has been deleted.
    '''
    try:
        delete_name = input("Who\'s contact would you like to delete?")
        if delete_name in data.keys():
            are_you_sure = input(f"Are you sure you want to delete the contact for {delete_name}? (y/n): ")
            if are_you_sure.lower() == 'y':
                data.pop(delete_name)
                print(f'Contact information for {delete_name} has been deleted.')
            else:
                print("Contact information has not been deleted. Returning to main menu.")
        else:
            print(f"{delete_name} is not a valid contact. Returning to main menu.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting...")
        sys.exit(1)
    except EOFError:
        print("\nUnexpected end of input. Exiting...")
        sys.exit(1)
    
def change_contact(data):
    change_name = input("Who\'s contact would you like to change?")
    if change_name in data.keys():
        are_you_sure = input(f"They\'re current number is listed as {data[change_name]}, are you sure you want to change it? (y/n): ")
        if are_you_sure.lower() == 'y':
            new_number = input("What is their new number? ")
            data[change_name] = new_number
        else:
            print("Returning to main menu.")
    else:
        print(f"{change_name} is not a valid contact. Returning to main menu.")
        
def search_contact(data):
    search_name = input("Who\'s contact are you searching for? ")
    search_name = search_name.lower()
    possible_contacts = [contact_name for contact_name in data.keys() if search_name in contact_name.lower()]
    print("Possible contacts:")
    for each in possible_contacts:
        print(f"{each}: {data[each]}")
    print("Returning to main menu.")
    
def save_file(data,file_location):
    save_over = input("Would you like to save over the existing file? (y/n): ")
    if save_over.lower() == 'y':
        print(f"Saving file to {file_location}.")
        with open(file_location,'w') as f:
            f.writelines(f"{key}: {data[key]}\n" for key in data.keys())
    else:
        save_location = input("Where would you like to save the file? ")
        # Do some error handling if the location doesn't exist or if the user doesn't have write access
        print(f"Saving file to {save_location}.")
        with open(save_location,'w') as f:
            f.writelines(f"{key}: {data[key]}\n" for key in data.keys())
                    
def confirm_exit():
    return input("Are you sure you want to exit? (y/n): ").lower() == 'y'
    
def main_menu():
    contact_file = greeting()
    try:
        data = open_file(contact_file)
    except SystemExit as e:
        print(f"Exited with code {e}")
    while True:
        print("(A) Add a contact")
        print("(R) Remove a contact")
        print("(C) Change a contact")
        print("(S) Search for a contact")
        print("(D) Display all")
        print("(V) Save file")
        print("(E) Save and exit")
        print("(X) Close program")
        user_inp = input("Please select an option:")
        user_inp = str.lower(user_inp)
        if user_inp == 'a':
            add_contact(data)
        elif user_inp == 'r':
            delete_contact(data)
        elif user_inp == 'c':
            change_contact(data)
        elif user_inp == 's':
            search_contact(data)
        elif user_inp == 'd':
            display_all(data)
        elif user_inp == 'v':
            save_file(data,contact_file)
        elif user_inp == 'e':
            if confirm_exit():
                save_file(data,contact_file)
                break
        elif user_inp == 'x':
            if confirm_exit():
                break
        else:
            print("Invalid choice. Please try again.")
        
        
if __name__ == "__main__":
    main_menu()