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
        current_frame = self._linked_frame
        while current_frame.has_next_frame():
            if current_frame.is_spare():
                total_score += current_frame.spare_bonus()
            elif current_frame.is_strike():
                total_score += current_frame.strike_bonus()
            total_score += current_frame.total_frame_score()
            current_frame = current_frame.next_frame

        if current_frame.is_spare():
            total_score += 10
            total_score += current_frame.spare_bonus()
        elif current_frame.is_strike():
            total_score += 10
            total_score += current_frame.strike_bonus()
        else:
            total_score += current_frame.total_frame_score()

        return total_score

    def _spare_bonus(self, index):
        '''
        Calculate the value of the next roll
        '''
        return self._linked_frame[index + 1].first_roll

    def _is_last_frame(self, index):
        '''
        Determine if last frame
        '''
        return index >= len(self._linked_frame) - 1

    def _strike_bonus(self, index):
        '''
        Calculate the value of the next two rolls
        '''
        next_index = index + 1
        total_frame_strike_bonus = self._linked_frame[next_index].total_frame_score()
        if self._is_strike_but_not_last_frame(next_index):
            total_frame_strike_bonus += self._linked_frame[next_index + 1].first_roll
        return total_frame_strike_bonus

    def _is_strike_but_not_last_frame(self, index):
        '''
        True if condition meets
        '''
        return (self._linked_frame[index].is_strike()
                and not self._is_last_frame(index))

    def __init__(self, linked_frame):
        '''
        Constructor
        '''
        self._linked_frame = linked_frame
