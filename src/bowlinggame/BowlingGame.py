'''
Created on 01/06/2013

@author: synion
'''

class BowlingGame(object):
    '''
    Calculates score for a bowling game
    '''

    def score(self, score_string):
        '''
        Calculates score from a string of rolls
        '''
        total_score = 0
        for character in score_string:
            total_score += int(character)
        return total_score

    def __init__(self):
        '''
        Constructor
        '''
        pass