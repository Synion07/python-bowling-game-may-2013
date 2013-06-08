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

    def __eq__(self, other):
        if isinstance(other, FinalFrame):
            if (self.first_roll == other.first_roll
                and self.second_roll == other.second_roll
                and self.third_roll == other.third_roll):
                return True

        return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        string = "<FinalFrame(" + str(self.first_roll)
        string += ", " + str(self.second_roll)
        string += ", " + str(self.third_roll) + ")>"
        return string

    def __init__(self, first_roll, second_roll, third_roll = 0):
        '''
        Constructor
        '''
        Frame.__init__(self, first_roll, second_roll)
        self.third_roll = third_roll

class LinkedFrame():
    '''
    A construction which has current frame and next frame
    '''

    def has_next_frame(self):
        '''
        return True if it has next frame linked
        '''
        return self.next_frame is not None

    def spare_bonus(self):
        '''
        Calculates spare bonus
        '''
        if self.has_next_frame():
            return self._next_frame_spare_bonus()
        else:
            return self._final_spare_bonus()
        
    def _next_frame_spare_bonus(self):
        '''
        Calculates spare bonus based on next frame
        '''
        return self.next_frame.current_frame.first_roll

    def strike_bonus(self):
        '''
        Calculates strike bonus
        '''
        total_bonus = 0
        if self.has_next_frame():
            if self.next_frame.is_strike():
                total_bonus += self._next_frame_is_strike_bonus()
            else:
                total_bonus += self._next_frame_is_not_strike_bonus()
        else:
            total_bonus += self._final_strike_bonus()
        return total_bonus
    
    def _next_frame_is_not_strike_bonus(self):
        '''
        Calculates next frame bonus, if it is not a strike
        '''
        return self.next_frame.total_frame_score()

    def _next_frame_is_strike_bonus(self):
        '''
        Calculates the strike bonus if the next frame
        is also a strike
        '''
        total_bonus = 0
        if self.next_frame.has_next_frame():
            total_bonus += self.next_frame.current_frame.first_roll
            total_bonus += self.next_frame.next_frame.current_frame.first_roll
        else:
            total_bonus += self.next_frame.current_frame.first_roll
            total_bonus += self.next_frame.current_frame.second_roll
        return total_bonus

    def is_spare(self):
        '''
        Calculates if current frame is spare
        '''
        return self.current_frame.is_spare()

    def is_strike(self):
        '''
        Calculates if current frame is strike
        '''
        return self.current_frame.is_strike()

    def total_frame_score(self):
        '''
        Returns current frame score
        '''
        return self.current_frame.total_frame_score()

    def _final_spare_bonus(self):
        '''
        Final frames are special calculating the bonus
        '''
        return self.current_frame.third_roll

    def _final_strike_bonus(self):
        '''
        Final frames are special calculating the bonus
        '''
        total_bonus = (self.current_frame.second_roll
                       + self.current_frame.third_roll)
        return total_bonus

    def __init__(self, frame, next_frame = None):
        '''
        A LinkedFrame knows about next frame
        '''
        self.current_frame = frame
        self.next_frame = next_frame

    def __eq__(self, other):
        if isinstance(other, LinkedFrame):
            if (self.next_frame == other.next_frame
                and self.current_frame == other.current_frame):
                return True

        return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        string = "<FinalFrame ("
        string += str(self.current_frame)
        string += ", "
        string += str(self.next_frame)
        string += ">"
        return string
