'''
Created on 01/06/2013

@author: synion
'''

class Frame(object):
    '''
    Represents a bowling frame (2 pins)
    '''
    
    def total_frame_score(self):
        '''
        Calculates total score in the frame
        '''
        return self.first_roll + self.second_roll
    
    def is_spare(self):
        '''
        Returns True if is a spare
        '''
        if not self.is_strike():
            return self.first_roll + self.second_roll == 10
        else:
            return False
    
    def is_strike(self):
        '''
        Returns True if it's a strike
        '''
        return self.first_roll == 10
    
    def __eq__(self, other):
        if isinstance(other, Frame):
            if (self.first_roll == other.first_roll 
                and self.second_roll == other.second_roll):
                return True
    
        return False
    
    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        string = "<Frame(" + str(self.first_roll) 
        string += ", " + str(self.second_roll) + ")>"
        return string

    def __init__(self, first_roll, second_roll):
        '''
        Constructor
        '''
        self.first_roll = first_roll
        self.second_roll = second_roll