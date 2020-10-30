# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 5 - GUI and card game using queue

from tkinter import *

# to use the queue FIFO
from queue import Queue

# to use the shuffle for shuffling the cards
from random import shuffle


class CardGame:

    # initialises the application
    def __init__(self):
        # set up game logic here:
        # shuffle the cards before first use
        # variable for holding the score
        self.player_score = 0
        self.the_cards = self.load_cards()
        self.init_window()

    # used by __init__
    # initialises the GUI window
    def init_window(self):
        root = Tk()
        root.geometry("300x200")
        root.title("Card Game")

        master_frame = Frame(master=root)
        master_frame.pack(expand=True)

        # frames hold the elements of the window
        # grid arranges the elements in a tabular manner
        # see mock-up screen in lab sheet for the layout design
        cards_frame = LabelFrame(master=master_frame)
        cards_frame.grid(row=0, column=0)
        button_frame = LabelFrame(master=master_frame)
        button_frame.grid(row=0, column=1)
        score_frame = LabelFrame(master=master_frame)
        score_frame.grid(row=1, column=0, columnspan=2)

        # add elements into the frames
        self.open_card = Button(cards_frame)
        the_card = PhotoImage(file=self.pick_card())
        self.open_card.config(image=the_card)
        self.open_card.grid(row=0, column=0, padx=2, pady=2)
        self.open_card.photo = the_card

        closed_deck = Button(cards_frame, command=self.pick_card)  # command= self.pick_card
        closed_card = PhotoImage(file='cards/closed_deck.gif')
        closed_deck.config(image=closed_card)
        closed_deck.grid(row=0, column=1, padx=2, pady=2)
        closed_deck.photo = closed_card

        done_button = Button(button_frame, text="I'm done!", command=self.done_playing)  # command=self.done_playing
        done_button.grid(row=0, column=0, pady=12)
        new_game_button = Button(button_frame, text="New Game", command=self.reset_game)  # command= self.reset_game
        new_game_button.grid(row=1, column=0, pady=13)
        exit_button = Button(button_frame, text="Exit", command=self.game_exit)
        exit_button.grid(row=2, column=0, pady=13)

        self.score_label = Label(score_frame, text="Your score: " + str(self.player_score), justify=LEFT)
        self.score_label.update_idletasks()
        self.score_label.pack()

        root.mainloop()

    # called by the exit_button Button
    # ends the GUI application
    def game_exit(self):
        exit()

    # helper function to load the cards
    # puts everything in a list first as it needs to be shuffled
    # returns a queue
    def load_cards(self):
        cards = Queue(maxsize=52)  # change this if you want to use a different data structure
        suits = ("hearts", "diamonds", "spades", "clubs")
        people = ("queen", "jack", "king")
        card_list = []

        # your code goes here:

        values = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')  # the numeric card values from 1 to 10

        # populating card_list
        for suit in suits:
            for value in values:
                card_list.append(value + "_" + suit)  # adding the numeric cards from each suit to the list card_list
            for person in people:
                card_list.append(person + "_" + suit)  # adding the queen/jack/king from each suit to card_list

        print("Shuffled deck of Cards:\n")

        shuffle(card_list)       # shuffle cards_list

        # print(len(card_list))

        print(list(dict.fromkeys(card_list)))       # removing duplicates from the list card_list

        # adding card_list elements to cards (queue)
        for i in range(0, 52):
            cards.put(card_list[i])

        # print("\n Cards in the queue: \n")
        # print(list(dict.fromkeys(cards.get()))) # printing the queue
        # print(cards.get(card_list)

        # print(cards.qsize()) # printing the size of the queue

        # checking whether the queue is full or not
        if cards.full():
            print("\nIs the queue full: ", cards.full())
        else:
            print("\nIs the queue empty: ", cards.empty())

        # # showing the score of the first card
        # picked_card = cards.get()
        # self.player_score = str(picked_card.split('_')[0])
        # print(self.player_score)

        # splitting the card list
        # for card in card_list:
        #     print(card.split('_'))

        return cards

    # called when clicking on the closed deck of cards
    # picks a new card from the card FIFO
    # updates the display
    # updates the score
    def pick_card(self):
        # print(self.the_cards.get())  # picking a random card from the queue as the player

        # updating the cards image

        current_card = self.the_cards.get()
        card_file = 'cards/' + current_card + '.gif'
        the_card = PhotoImage(file=card_file)
        self.open_card.config(image=the_card)
        self.open_card.photo = the_card
        # self.open_card.update_idletasks()

        # trying to load the value of the current card on the screen when the game is loaded, by splitting list
        picked_card = current_card

        if str(picked_card.split('_')[0]) == 'queen':
            self.player_score = int(self.player_score + 10)
        elif str(picked_card.split('_')[0]) == 'jack':
            self.player_score = int(self.player_score + 10)
        elif str(picked_card.split('_')[0]) == 'king':
            self.player_score = int(self.player_score + 10)
        else:
            self.player_score = self.player_score + int(picked_card.split('_')[0])
            print(self.player_score)

        self.check_scores()

        return card_file

    # contains the logic to compare if the score
    # is smaller, greater or equal to 21
    # sets a label
    def check_scores(self):
        if self.player_score == 21:
            print("You scored a Jackpot!!")
            # self.reset_game()
        elif self.player_score < 21:
            # self.done_playing()
            print("Well Done! You scored: ", self.player_score)
        else:
            print("You scored over 21, Hard Luck!")
            # self.game_exit()

    # calculates the new score
    # takes a card argument of type
    def update_score(self, card):
        pass  # replace this line by your code

    # this method is called when the "Done" button is clicked
    # it means that the game is over and we check the score
    # but we don't allow any further game play. When clicking
    # on the closed deck after this button is pressed, nothing
    # should happen. Only options are to ask for a new game or
    # exit the program after this button was pressed.
    def done_playing(self):
        print("This button works")

        self.check_scores()

    # this method is called when the "New Game" button is clicked
    # resets all variables
    # sets the game's cards to the initial stage, with a freshly
    # shuffled card deck
    def reset_game(self):
        # resetting the player score to 0
        self.player_score = 0

        # restarting the game by calling load_card()
        self.the_cards = self.load_cards()
        self.pick_card()

# object creation here:


app = CardGame()
