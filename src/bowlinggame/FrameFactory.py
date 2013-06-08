'''
Created on 01/06/2013

@author: synion
'''
from bowlinggame.Frame import Frame, FinalFrame

class FrameFactory(object):
    '''
    Converts a string of rolls into a list of Frames
    '''

    def build_frame(self, frame_input):
        '''
        Builds a single frame
        '''
        if frame_input == "X-":
            return Frame(10, 0)
        else:
            return Frame(int(frame_input[0]), int(frame_input[1]))
        
    def build_final_frame(self, frame_input):
        '''
        Builds the final frame
        '''
        converted_frame = []
        for character in frame_input:
            if character == 'X':
                converted_frame += [10]
            else:
                converted_frame += [int(character)]
        if len(converted_frame) == 3:
            return FinalFrame(converted_frame[0], converted_frame[1], 
                              converted_frame[2])
        else:
            return FinalFrame(converted_frame[0], converted_frame[1])
    
    def build_game(self, game_string):
        '''
        Builds a full game
        '''
        frame_list = [game_string[i:i+2] for i in range(0, 18, 2)]
        converted_frames = []
        for frame in frame_list:
            converted_frames += [self.build_frame(frame)]
        converted_frames += [self.build_final_frame(game_string[18:])]
        return converted_frames

    def __init__(self):
        '''
        Constructor
        '''
        pass
