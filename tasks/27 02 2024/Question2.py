
# Create a class for creating and writing data to a text file. The class must have __enter__ and __exit__ 
# defined. 
# __enter__ must use the built in `open` to open the file and set the file pointer to self. 
# __exit__ must close the file pointer on exit. 
# If the user entered text contains the word 'bug' then __exit__ must delete the file on exiting. 
# Or if any exception has occurred, then also __exit__ must delete the file.(remember to close file 
# before deleting) 
# Use a `with` block to execute the logic. 



class TextFileHandler:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
 
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except Exception as e:
            print(f"Error: {e}")
            raise
 
        return self
 
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
 
        if exc_type is not None or 'bug' in self.file.read():
            try:
                import os
                os.remove(self.filename)
                print(f"File '{self.filename}' deleted.")
            except Exception as e:
                print(f"Error in deleting file: {e}")
 
if __name__ == "__main__":
    try:
        with TextFileHandler('newfiletodelete.txt') as handler:
            handler.file.write("This is a sample text without bug.")
           
            raise Exception("Test Exception") # Uncomment the line to delete the file
    except Exception as e:
        print(f"An exception occurred: {e}")