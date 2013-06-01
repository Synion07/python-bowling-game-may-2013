'''
Created on 01/06/2013

@author: synion
'''
from Frame import Frame
from FrameFactory import FrameFactory

class BowlingGame(object):
    '''
    Calculates score for a bowling game
    '''

    def score(self, score_string):
        '''
        Calculates score from a string of rolls
        '''
        total_score = 0
        last_score = 0
        for character in score_string:
            current_score = int(character)
            total_score += current_score
            if last_score == current_score:
                total_score += 5
            last_score = current_score
        return total_score

    def __init__(self):
        '''
        Constructor
        '''
        pass
