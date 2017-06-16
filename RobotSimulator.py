class RobotSimulator:

    def __init__(self, f_direction, x, y):
        self.direction = f_direction
        self.x_pos = x
        self.y_pos = y

    def advance(self):
        if (self.direction == 'N'):
            self.y_pos += 1

        elif (self.direction == 'S'):
            self.y_pos -= 1

        elif (self.direction == 'E'):
            self.x_pos += 1

        elif (self.direction == 'W'):
            self.x_pos -= 1

        return self.x_pos, self.y_pos

    def turn_right(self):
        if (self.direction == 'N'):
            self.direction = 'E'

        elif (self.direction == 'S'):
            self.direction = 'W'

        elif (self.direction == 'E'):
            self.direction = 'S'

        elif (self.direction == 'W'):
            self.direction = 'N'

        return self.direction

    def turn_left(self):
        if (self.direction == 'N'):
            self.direction = 'W'

        elif (self.direction == 'S'):
            self.direction = 'E'

        elif (self.direction == 'E'):
            self.direction = 'N'

        elif (self.direction == 'W'):
            self.direction = 'S'

        return self.direction

    def navigate_robot(self, command_string):

        for letter in command_string:
            if (letter.upper() == 'A'):
                print(self.advance())
            elif (letter == 'R'):
                print(self.turn_right())
            elif (letter == 'L'):
                print(self.turn_left())

robot = RobotSimulator('N', 5, 0)
robot.navigate_robot('ARRAL')
