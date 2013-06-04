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

class FinalFrame(Frame):
    '''
    The final frame is a boundary case, with three rolls
    '''
    
    def is_second_roll_strike(self):
        '''
        Determines whether the second roll is a strike
        '''
        return self.second_roll == 10
    
    def spare_bonus(self):
        '''
        Final frames are special calculating the bonus
        '''
        return self.third_roll
    
    def strike_bonus(self):
        '''
        Final frames are special calculating the bonus
        '''
        total_bonus = self.second_roll + self.third_roll
        if self.is_second_roll_strike():
            total_bonus += self.third_roll
        return total_bonus
    
    def __repr__(self):
        string = "<FinalFrame(" + str(self.first_roll)
        string += ", " + str(self.second_roll) 
        string += ", " + str(self.third_roll) + ")>"
        return string

    def __init__(self, first_roll, second_roll, third_roll):
        '''
        Constructor
        '''
        Frame.__init__(self, first_roll, second_roll)
        self.third_roll = third_roll
