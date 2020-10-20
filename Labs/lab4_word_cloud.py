# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: Oct 2020
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurrence of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 10px">Four score</span>')
        fo.write('<span style="font-size: 60px">and</span>')
        fo.write('<span style="font-size: 10px">seven </span>')
        fo.write('<span style="font-size: 10px">ago </span>')
        fo.write('<span style="font-size: 20px">our </span>')
        fo.write('<span style="font-size: 10px">fathers brought fourth </span>')
        fo.write('<span style="font-size: 20px">on </span>')
        fo.write('<span style="font-size: 30px">this </span>')
        fo.write('<span style="font-size: 10px">continent </span>')
        fo.write('<span style="font-size: 70px">a</span>')
        fo.write('<span style="font-size: 20px"> new </span>')
        fo.write('<span style="font-size: 10px">nation </span>')
        fo.write('<span style="font-size: 20px">conceived </span>')
        fo.write('<span style="font-size: 40px">in </span>')
        fo.write('<span style="font-size: 10px">liberty </span>')
        fo.write('<span style="font-size: 40px">dedicated </span>')
        fo.write('<span style="font-size: 80px">to </span>')
        fo.write('<span style="font-size: 90px">the </span>')
        fo.write('<span style="font-size: 10px">proposition </span>')
        fo.write('<span style="font-size: 130px">that </span>')
        fo.write('<span style="font-size: 10px">all </span>')
        fo.write('<span style="font-size: 10px">men </span>')
        fo.write('<span style="font-size: 30px">are </span>')
        fo.write('<span style="font-size: 10px">created </span>')
        fo.write('<span style="font-size: 10px">equal. </span>')
        fo.write('<span style="font-size: 10px"> Now </span>')
        fo.write('<span style="font-size: 80px">we </span>')
        fo.write('<span style="font-size: 10px">engaged </span>')
        fo.write('<span style="font-size: 30px">great </span>')
        fo.write('<span style="font-size: 10px">civil war testing whether</span>')
        fo.write('<span style="font-size: 40px">nation </span>')
        fo.write('<span style="font-size: 20px">or </span>')
        fo.write('<span style="font-size: 10px">any </span>')
        fo.write('<span style="font-size: 20px">so can long </span>')
        fo.write('<span style="font-size: 10px">endure </span>')
        fo.write('<span style="font-size: 20px">We </span>')
        fo.write('<span style="font-size: 10px">met battlefield </span>')
        fo.write('<span style="font-size: 50px">of </span>')
        fo.write('<span style="font-size: 10px"> war. </span>')
        fo.write('<span style="font-size: 50px">have </span>')
        fo.write('<span style="font-size: 10px">come dedicate portion field as final resting-place </span>')
        fo.write('<span style="font-size: 50px">for </span>')
        fo.write('<span style="font-size: 10px">those </span>')
        fo.write('<span style="font-size: 30px">who </span>')
        fo.write('<span style="font-size: 60px">here </span>')
        fo.write('<span style="font-size: 20px">gave </span>')
        fo.write('<span style="font-size: 10px">their lives might live. </span>')
        fo.write('<span style="font-size: 30px">It </span>')
        fo.write('<span style="font-size: 30px">is </span>')
        fo.write('<span style="font-size: 10px">altogether fitting proper should do this. </span>')
        fo.write('<span style="font-size: 10px">But larger sense </span>')
        fo.write('<span style="font-size: 30px">cannot </span>')
        fo.write('<span style="font-size: 10px">dedicate consecrate hallow ground. </span>')
        fo.write('<span style="font-size: 20px">The </span>')
        fo.write('<span style="font-size: 10px">brave men </span>')
        fo.write('<span style="font-size: 20px">living </span>')
        fo.write('<span style="font-size: 30px">dead </span>')
        fo.write('<span style="font-size: 10px">struggled consecrated </span>')
        fo.write('<span style="font-size: 20px">it far </span>')
        fo.write('<span style="font-size: 10px">above poor power add detract. world will little note nor </span>')
        fo.write('<span style="font-size: 10px">remember </span>')
        fo.write('<span style="font-size: 20px">what </span>')
        fo.write('<span style="font-size: 10px">say here but never forget </span>')
        fo.write('<span style="font-size: 30px">they </span>')
        fo.write('<span style="font-size: 10px">did here. </span>')
        fo.write('<span style="font-size: 30px">us </span>')
        fo.write('<span style="font-size: 20px">rather be </span>')
        fo.write('<span style="font-size: 10px">unfinished work </span>')
        fo.write('<span style="font-size: 20px">which </span>')
        fo.write('<span style="font-size: 10px">fought thus nobly advanced task remaining before </span>')
        fo.write('<span style="font-size: 20px">-- from these </span>')
        fo.write('<span style="font-size: 10px">honored take increased </span>')
        fo.write('<span style="font-size: 20px">devotion </span>')
        fo.write('<span style="font-size: 10px">cause last full measure highly resolve </span>')
        fo.write('<span style="font-size: 30px">shall </span>')
        fo.write('<span style="font-size: 20px>not </span>')
        fo.write('<span style="font-size: 10px">died vain under God birth freedom government </span>')
        fo.write('<span style="font-size: 20px">people </span>')
        fo.write('<span style="font-size: 10px">by people perish earth.</span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()

    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}

        # your code goes here:
        with open('gettisburg.txt', 'r') as file:

            # reading each line of gettisburg.txt line by line

            for line in file:

                # reading each line and printing
                for word in line.split():

                    # reading each word
                    # seeing if the word is in the dictionary
                    if word in my_dict:
                        my_dict[word] = my_dict[word] # If the current is in the dictionary already

                    else:
                        my_dict[word] = 1 # then

                    print(my_dict)

                    self.add_to_dict(word, my_dict)

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurrence counter to 1
    # returns a dictionary
    def add_to_dict(self, current_word, the_dict):
        # your code goes here

        i = 0

        for word in the_dict: # getting all the keys
            print(current_word)

            if i != len(the_dict) - 1:

                if current_word == word:
                    the_dict[word] = the_dict[word] + 1

                print(word)

            i = i + 1

        return the_dict


wc = WordCloud()
