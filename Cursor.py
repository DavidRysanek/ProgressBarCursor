class Cursor:
    # https://en.m.wikipedia.org/wiki/ANSI_escape_code

    # Control characters
    
    # '\x1b' == '\033' == ESCAPE

    UP = '\033[1A'
    UP_N = '\033[%dA'
    DOWN='\033[1B'
    DOWN_N='\033[%dB'
    RIGHT='\033[1C'
    RIGHT_N='\033[%dC'
    LEFT='\033[1D'
    LEFT_N='\033[%dD'

    MOVE_TO='\033[%d;%dH'
    TAB = '\t'
    NEW_LINE = '\n'
    BOL = '\r' # beginning_of_line
    # Erases part of the line.
    # If n is 0 (or missing), clear from cursor to the end of the line.
    # If n is 1, clear from cursor to beginning of the line.
    # If n is 2, clear entire line. Cursor position does not change.
    ERASE_TO_END_OF_LINE = '\033[0K'
    ERASE_TO_BEGINNING_OF_LINE = '\033[1K'
    ERASE_ENTIRE_LINE = '\033[2K'
    ERASE_LINE_N = '\033[%dK'

    SAVE_POSITION='\033[s'
    RESTORE_POSITION='\033[u'


    def moveto(x, y):
        # Using ANSI escape sequence, where ESC[y;xH moves curser to row y, col x:
        print(Cursor.MOVE_TO % (y, x), end='')

    def up(n=1):
        print(Cursor.UP_N % (n), end='')

    def down(n=1):
        print("\033[%dB" % (n), end='')

    def right(n=1):
        print(Cursor.RIGHT_N % (n), end='')

    def left(n=1):
        print(Cursor.LEFT_N % (n), end='')

    # carriage_return
    # Moves the cursor to column zero.
    def beginning_of_line():
        print(Cursor.BOL, end='')

    def new_line():
        print(Cursor.NEW_LINE, end='')


    def erase_line():
        print(Cursor.ERASE_ENTIRE_LINE, end='')

    def erase_to_beginning_of_line():
        print(Cursor.ERASE_TO_BEGINNING_OF_LINE, end='')

    def erase_to_end_of_line():
        print(Cursor.ERASE_TO_END_OF_LINE, end='')



    def save_position():
        print(Cursor.SAVE_POSITION, end='')

    def restore_position():
        print(Cursor.RESTORE_POSITION, end='')


    def print(text=''):
        print(text, end='')

    def println(text=''):
        print(text)


    def demo():
        self = Cursor
        for i in range(5):
            self.println('|----------|----------|')

        self.save_position()
        self.print('Bye!')
        self.beginning_of_line()
        self.up(4)
        self.right(9)
        self.print('o')
        self.up(1)
        self.right(1)
        self.print('T')
        self.down()
        self.right(1)
        self.print('O')
        self.restore_position()
        self.println('')

        # https://docs.python.org/3.8/library/curses.html#curses.getsyx
        # cursor.moveto(11, 8)
        # (x, y) = curses.getsyx()
        # cursor.restore_position()
        # print(x)
        # print(y)


if __name__ == "__main__":
    Cursor.demo()