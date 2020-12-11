# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.

    ...

    Attributes:
    -----

        characters : list
        an empty list. To hold the characters passed into the class

        cursor: int
        initialised to 0

        filename: document (txt file)
        a txt file that shows the changes made in this file in lab_t2.txt

    """

    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name

    @property
    def getting_steps(self):
        return steps

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        del self.characters[self.cursor]

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method forwards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        self.cursor -= steps

        # if the nunmber of steps passed greater than 0 change the value of cursor to 0 to insert at the begining of the characters in the text file
        # trying to catch errors
        try:
            if steps > 0:
                self.cursor = 0

        except:
            print("Program Crashed.")


# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

doc.backward(44)
doc.delete()
doc.insert('n')
doc.save()
print(doc.cursor)

