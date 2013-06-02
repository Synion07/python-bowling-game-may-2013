'''
Created on 01/06/2013

@author: synion
'''
from Frame import Frame

class BowlingGame(object):
    '''
    Calculates score for a bowling game
    '''

    def score(self):
        '''
        Calculates score from a string of rolls
        '''
        total_score = 0
        for index, frame in enumerate(self._frames):
            if frame.is_spare():
                total_score += self._frames[index + 1].first_roll
            elif frame.is_strike():
                total_score += self._two_next_rolls(index)
            total_score += frame.total_frame_score()
        return total_score

    def _two_next_rolls(self, index):
        '''
        Calculate the value of the next two rolls
        '''
        two_roll_score = self._frames[index + 1].total_frame_score()
        if self._frames[index + 1].is_strike():
            two_roll_score += self._frames[index + 2].first_roll
        return two_roll_score

    def __init__(self, frames):
        '''
        Constructor
        '''
        self._frames = frames
