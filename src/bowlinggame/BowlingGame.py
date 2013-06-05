'''
Created on 01/06/2013

@author: synion
'''

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
            if self._is_last_frame(index):
                if frame.is_strike():
                    total_score += 10
                    total_score += frame.strike_bonus()
                else:
                    if frame.is_spare():
                        total_score += frame.spare_bonus()
                    total_score += frame.total_frame_score()
            else:
                if frame.is_spare():
                    total_score += self._spare_bonus(index)
                elif frame.is_strike():
                    total_score += self._strike_bonus(index)
                total_score += frame.total_frame_score()
        return total_score

    def _spare_bonus(self, index):
        '''
        Calculate the value of the next roll
        '''
        return self._frames[index + 1].first_roll

    def _is_last_frame(self, index):
        '''
        Determine if last frame
        '''
        return index >= len(self._frames) - 1

    def _strike_bonus(self, index):
        '''
        Calculate the value of the next two rolls
        '''
        next_index = index + 1
        total_frame_strike_bonus = self._frames[next_index].total_frame_score()
        if self._is_strike_but_not_last_frame(next_index):
            total_frame_strike_bonus += self._frames[next_index + 1].first_roll
        return total_frame_strike_bonus
    
    def _is_strike_but_not_last_frame(self, index):
        '''
        True if condition meets
        '''
        return (self._frames[index].is_strike() 
                and not self._is_last_frame(index))

    def __init__(self, frames):
        '''
        Constructor
        '''
        self._frames = frames
