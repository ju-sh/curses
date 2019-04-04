import curses

CELL_WIDTH = 17
CELL_HEIGHT = 16
DEBUG = True

def cell(win, y, x):
	win.hline(0, 1 , curses.ACS_HLINE, CELL_WIDTH-1)
	if DEBUG:
		win.getch()
	win.addch(0, CELL_WIDTH, curses.ACS_URCORNER)
	if DEBUG:
		win.getch()
	win.vline(1, CELL_WIDTH, curses.ACS_VLINE, CELL_HEIGHT)
	if DEBUG:
		win.getch()
	win.addch(CELL_HEIGHT+1, CELL_WIDTH, curses.ACS_LRCORNER)
	if DEBUG:
		win.getch()
	win.hline(CELL_HEIGHT+1, CELL_WIDTH-(CELL_WIDTH-1), curses.ACS_HLINE, CELL_WIDTH-1)
	if DEBUG:
		win.getch()
	win.addch(CELL_HEIGHT+1, 0, curses.ACS_LLCORNER)
	if DEBUG:
		win.getch()
	win.vline(1, 0, curses.ACS_VLINE, CELL_HEIGHT)
	if DEBUG:
		win.getch()
	win.addch(0, 0, curses.ACS_ULCORNER)

class MainClass:
	def __init__(self):
		curses.wrapper(self.driver_fn)

	def driver_fn(self, stdscr):
		stdscr.clear()

		height, width = stdscr.getmaxyx()
		stdscr.addstr(0, 0, f"{height}, {width}")
		stdscr.addstr(height//2, width//2, "Johnny ate sugar. Opened his mouth and laughed at his Pa.")

		cell(stdscr, 2,3)

		stdscr.refresh()
		stdscr.getch()

if __name__=="__main__":
	MainClass()
