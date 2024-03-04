# . Create a class named Notes for handling text-based file operations. Class 
# should contain methods "write", "read" and then "append" as instance 
# methods or class methods. (Can contain any other methods if you wish) 
# Use a single file for saving the notes. You can set the file name as a constant 
# somewhere in the program (Or as a class variable). write method should 
# create the if it doesn't exist, Then it should overwrite the older contents 
# with the user input if the user plans to overwrite the file. read method 
# should read the whole file contents and return it. If the file doesn't exist, 
# then it should return "No notes found" append method should take the 
# user input value and it must add the value to the end of the file. It must not 
# overwrite the file. Now create a program to utilize this class.  
# The program should repeatedly ask the user for these 4 choices :  
# 1 - Write Note (Overwrite existing).  
# 2 - Add more Notes (Append).  
# 3 - Read Notes.  
# 4 – Exit




class Notes:
    FILENAME = "notes.txt"  # Constant file name

    @classmethod
    def write(cls):
        with open(cls.FILENAME, "w") as file:
            note = input("Enter your note: ")
            file.write(note) # to write notes
            print("Note written successfully.")

    @classmethod
    def read(cls):
        try:
            with open(cls.FILENAME, "r") as file:
                return file.read() #class method to read notes
        except FileNotFoundError:
            return "No notes found."

    @classmethod
    def append(cls):
        """Method to append notes to the file."""
        with open(cls.FILENAME, "a") as file: #class method to append notes
            note = input("Enter additional note: ")
            file.write("\n" + note)
            print("Note appended successfully.")

# Program to utilize the Notes class
def main():
    while True:
        print("\nOptions:")
        print("1 - Write Note (Overwrite existing)")
        print("2 - Add more Notes (Append)")
        print("3 - Read Notes")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            Notes.write()
        elif choice == "2":
            Notes.append()
        elif choice == "3":
            print(Notes.read())
        elif choice == "4":
            print("YOU HAVE EXITES FROM THE NOTEPAD SOFTWARE")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
