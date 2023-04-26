import time
print("These is test statement")


class tictactoe:
    # when the constructor will be called that time the initial that is empty state is also called
    def __init__(self):
        self.initialstate()
    # these is the initial state which will called when object of the tictactoe is created

    def initialstate(self):
        self.intstate = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        # by default the first turn is of x player
        self.player = 'X'

    def print_board(self):
        for x in range(0, 3):
            for y in range(0, 3):
                # print(self.intstate[x][y], end=" ")
                print('{}|'.format(self.intstate[x][y], end=" "))
            print()
        print()

    def checkvalid(self, posn_x, posn_y):
        # check if we go beyond the position or not
        if posn_x < 0 or posn_x > 2 or posn_y < 0 or posn_y > 2:
            return False
        # check if the current postion is fill or not
        elif self.intstate[posn_x][posn_y] != '.':
            return False
        # if all is satisfied then return the true
        else:
            return True

    def checkwin(self):
        for i in range(0, 3):
            # if it has vertical state
            # [0,0][1,0][2,0]
            if(self.intstate[0][i] != '.' and self.intstate[0][i] == self.intstate[1][0] and self.intstate[1][i] == self.intstate[2][i]):
                return self.intstate[0][i]

        # if it has horizontal state
        for i in range(0, 3):
            if self.intstate[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.intstate[i] == ['O', 'O', 'O']:
                return 'O'
        # check the diagonal from top left to right bottom
        if(self.intstate[0][0] != '.' and self.intstate[0][0] == self.intstate[1][1] and self.intstate[0][0] == self.intstate[2][2]):
            return self.intstate[0][0]
        # check the diagonal from top right to left bottom
        if(self.intstate[0][2] != '.' and self.intstate[0][2] == self.intstate[1][1] and self.intstate[0][2] == self.intstate[2][0]):
            return self.intstate[0][2]

        # check if the board is full or not
        for i in range(0, 3):
            for j in range(0, 3):
                if(self.intstate[i][j] == '.'):
                    return None
        return '.'

    def check_maxs_move(self, alpha, beta):

        x_val = None
        y_val = None
        store_result = self.checkwin()
        # initially assigning the value to variable
        maxvalue = -2
        # loss
        if store_result == 'X':
            return (-1, 0, 0)
        # win
        elif store_result == 'O':
            return (1, 0, 0)
        # tie
        elif store_result == '.':
            return (0, 0, 0)

        for x in range(0, 3):
            for y in range(0, 3):
                if(self.intstate[x][y] == '.'):
                    # on the empty field 'O' makes the move and calls the min function which is nex branch
                    self.intstate[x][y] == 'O'
                    (m, min_vone, min_vtwo) = self.check_min_move(alpha, beta)
                    if m > maxvalue:
                        maxvalue = m
                        x_val = x
                        y_val = y
                    self.intstate[x][y] = '.'
                    if maxvalue >= beta:
                        return (maxvalue, x_val, y_val)
                    if maxvalue > alpha:
                        alpha = maxvalue

        return (maxvalue, x_val, y_val)

    
    #Making the min fuction to check the move
    def check_min_move(self, alpha, beta):
        x_val = None
        y_val = None
        store_result = self.checkwin()
        minvalue = 2
        #if res IS WINNING 
        if store_result == 'X':
            return (-1, 0, 0)

        elif store_result == 'O':
            return (1, 0, 0)
        elif store_result == '.':
            return (0, 0, 0)

        for x in range(0, 3):
            for y in range(0, 3):
                if(self.intstate[x][y] == '.'):
                    self.intstate[x][y] == 'X'
                    (m, min_vone, min_vtwo) = self.check_maxs_move(alpha, beta)
                    if m < minvalue:
                        minvalue = m
                        x_val = x
                        y_val = y
                    self.intstate[x][y] = '.'
                    if minvalue <= alpha:
                        return (minvalue, x_val, y_val)
                    if minvalue < beta:
                        beta = minvalue

        return (minvalue, x_val, y_val)

    def playgame(self):
        while True:
            self.print_board()
            self.result = self.checkwin()

            if self.result != None:
                if self.result == 'X':
                    print('X is winner')
                elif self.result == 'O':
                    print('O is winner')
                elif self.result == '.':
                    print('Tie')

                self.initialstate()
                return

            if self.player == 'X':

                while True:
                    (store_m, movx, movy) = self.check_min_move(-2,2)
                    px = int(input('Enter the x coordinate'))
                    py = int(input('Enter the y coordinate'))

                    (movx, movy) = px, py

                    if self.checkvalid(px, py):
                        self.initialstate[px][py] = 'X'
                        self.player = 'O'
                        break
                    else:
                        print('Invalid move')
            else:
                (store_m, movx, movy) = self.check_maxs_move()
                self.intstate[px][py] = 'O'
                self.player = 'X'


def main():
    g = tictactoe()
    g.playgame()


if __name__ == "__main__":
    main()
