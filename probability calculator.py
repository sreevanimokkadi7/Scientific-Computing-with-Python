import copy
import random

class Hat:

    def __init__(self, **kwargs):
        '''Contents should be a list of strings containing one item for each ball in the hat.'''
        self.contents = []
        for k, v in kwargs.items():
            self.contents.extend([k] * v)

    def draw(self, draw_num):
        '''Draw method that accepts an argument indicating the number of balls to draw from the hat. Remove balls at random from contents list and return those balls as a list of strings. The balls should not go back into the hat during the draw, similar to an urn experiment without replacement. If the number of balls to draw exceeds the available quantity, return all the balls.'''
        draw_list = []
        if draw_num <= len(self.contents):
            for _ in range(draw_num):
                random_ball = random.randint(0, len(self.contents)-1)
                draw_list.append(self.contents[random_ball])
                self.contents.remove(self.contents[random_ball])
        else:
            draw_list = self.contents[:]
            self.contents.clear()
        
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)

        drawn={}
        for ball in drawn_balls:
            if ball in drawn:
                drawn[ball] += 1
            else:
                drawn[ball] = 1
            
        count = True
        for color, count in expected_balls.items():
            if drawn.get(color, 0) < count:
                count = False
                break
        if count:
            M += 1
        
    return M / num_experiments
