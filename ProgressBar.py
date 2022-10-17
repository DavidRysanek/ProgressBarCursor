from Cursor import Cursor as cursor

class ProgressBar:

    def __init__(self, width=40, title='Progress', emptyChar='░', fillChar='▓', openingChar='║', closingChar='║'):
        self.width = width
        self.title = title
        self.emptyChar = emptyChar
        self.fillChar = fillChar
        self.openingChar = openingChar
        self.closingChar = closingChar
        self.update(0)

    def update(self, percent, message='', title=''):
        # prepare current line
        cursor.beginning_of_line()
        # calculate number of chars
        done = int(self.width * percent)
        notDone = int(self.width - done)
        # print the progress bar
        cursor.print('%s %s%s%s%s %d%% %s' % (title or self.title, self.openingChar, self.fillChar*done, self.emptyChar*notDone, self.closingChar, int(100*percent), message))
        # erare rest of the line
        cursor.erase_to_end_of_line()

    def demo():
        from time import sleep

        bar = ProgressBar()
        for i in range(0, 101):
            bar.update(float(i / 100), title='Processing file %d/100' % i)
            sleep(0.03)


if __name__ == "__main__":
    ProgressBar.demo()