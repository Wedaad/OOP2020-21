# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        __my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            __my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            __my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self.__my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: "+self.the_words)

class WordDuplication(WordGames): # you implement this and provide docstrings
    pass


class WordScramble(WordGames):  # you implement this and provide docstrings
    def __init__(self, user_sentence):
        super().__init__()
        self.__my_words = user_sentence
        
    def scramble_word(self):
        self.__my_words = input("Please enter a word or sentence: ")

        # # if the sentence is longer that 3 characters
        # if len(self.__my_words) > 3:
        #     new_word = self.__my_words[0] + self.__my_words[2] + self.__my_words[1]
        # elif len(self.__my_words) <= 3:  # If the sentence is shorter that 3 characters
        #     new_word = self.__my_words
        # else: # the sentence is just one character long
        #     print("try again")
        #     new_word = False
        # print(new_word)

        # scrambling one full sentence
        sentence = self.__my_words.strip().split()

        # getting the words from the sentence
        for index, word in enumerate(sentence):
            # checking if the length of the word is greater than 3 characters
            if len(word) > 3:
                # swapping the indices of the 2nd and last element
                temp_word = list(word)  # list() creates a list object
                if (',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    # split the word into a list of characters and swap them around
                    # this swap leaves the first and the last letters intact
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                # joining the characters together to form a scrambled word
                scrambled_word = ''.join(temp_word)

                # replacing the previous word at the position with new scrambled word
                sentence[index] = scrambled_word

            else:  # If the length of the word is less than 3 then you dont need to scramble it
                sentence[index] = word

        # Join the sentence back together in a scrambled state
        new_sentence = ''.join(sentence)

        # print the scrambled sentence
        print(new_sentence)


# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)

# Create an instances of the classes here:
wg = WordGames()
wg.word_play()
word_scramble = WordScramble()
word_scramble.scramble_word()

