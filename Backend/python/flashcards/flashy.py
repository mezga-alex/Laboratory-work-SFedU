# oop

"""
to do:

1. unit tests
2. questions right vs questions wrong
3. timer
4. display questions at the end (that the user got wrong) with their right answer
5. make sure you don't repeat options (recursive function)
6. error handling - input (must be number!)

"""

from os import system, name
from random import randint
import sys

class FlashCards(object):

    def __init__(self, answers_file, questions_file):
        self.questions_file = questions_file
        self.answers_file = answers_file

    def clear_screen(self):
        """ clears the screen """
        system(['clear','cls'][name == 'nt'])

    def read_files(self):

        """ 
        opens the question and answer files
        then parses them line by line
        """

        content_list = []

        file1_content = self.questions_file.readlines()
        file2_content = self.answers_file.readlines()

        content_list.extend([file1_content, file2_content])
        return content_list

    def display_question(self, content):
        
        """
        displays question, list of potential answers (options)
        returns question, options, and user answer in a list
        """

        question = randint(0, len(content[0])-1)
        print "\nUnit Test:", content[0][question], ''
        options = [randint(0, len(content[1])-1),
        randint(0, len(content[1])-1),
        randint(0, len(content[1])-1)]
        options[randint(0,2)] = question
        print '1: ', content[1][options[0]],
        print '\n2: ', content[1][options[1]],
        print '\n3: ', content[1][options[2]],

        answer = input('\nYour choice: ')

        answers_list = []
        answers_list.extend([options,answer,question])
        return answers_list

    def check_if_correct(self, options_question_answer_list):

        """ determines if user answer is correct """
        if options_question_answer_list[0][options_question_answer_list[1]-1] == options_question_answer_list[2]:
            return '\nCorrect!'
        else:
            return '\nIncorrect!!'

    def play_again(self):
        again = raw_input('\nPress Enter to continue (or x then Enter to exit) ...')
        return again



# if __name__ == '__main__':
#     count = 0
#     score = 0
#     again = 0
#     file1 = open('questions.txt', 'r')
#     file2 = open('answers.txt', 'r')
#     create = FlashCards(file1, file2)
#     data = create.read_files()
#     create.clear_screen()
#     while True:
#         if again == "x":
#             sys.exit() 
#         else:
#             answers = create.display_question(data)
#             correct = create.check_if_correct(answers)
#             if correct == '\nCorrect!':
#                 score += 1
#             print '\nYour score is {}'.format(score)
#             again = create.play_again()
#             count += 1
#             create.clear_screen()


