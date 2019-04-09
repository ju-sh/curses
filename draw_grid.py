import curses

CELL_WIDTH = 3 # Meaning width of cell excluding the corners
CELL_HEIGHT = 1
DEBUG = True

def drawGrid(win, y, x, cell_width, cell_height, cols, rows):
	# Corners
	win.addch(y+0, x+0, curses.ACS_ULCORNER)	
	win.addch(y+0, x+(cell_width+1)*cols, curses.ACS_URCORNER)	
	win.addch(y+(cell_height+1)*rows, x+0, curses.ACS_LLCORNER)	
	win.addch(y+(cell_height+1)*rows, x+(cell_width+1)*cols, curses.ACS_LRCORNER)	
		
	# For top and bottom tees
	for i in range(1, cols):
		# Top tee
		win.addch(y+0, x+(cell_width+1)*i, curses.ACS_TTEE)
		# Bottom tee
		win.addch(y+(cell_height+1)*rows, x+(cell_width+1)*i, curses.ACS_BTEE)
	
	# For plus (or crosses or junctions)
	for i in range(1, rows):
		for j in range(1, cols):
			win.addch(y+(cell_height+1)*i, x+(cell_width+1)*j, curses.ACS_PLUS)

	# For left and right tees
	for i in range(1, rows):
		# Left tee
		win.addch(y+(cell_height+1)*i, x+0, curses.ACS_LTEE)
		# Right tee
		win.addch(y+(cell_height+1)*i, x+(cell_width+1)*cols, curses.ACS_RTEE)

	# Vertical bars
	for i in range(rows):
		for j in range(cols+1):
			win.vline(y+1+(cell_height+1)*i, x+(cell_width+1)*j, curses.ACS_VLINE, cell_height)	
				
	# Horizontal bars
	for i in range(rows+1):
		for j in range(cols):
			win.hline(y+(cell_height+1)*i, x+1+(cell_width+1)*j, curses.ACS_HLINE, cell_width)	

class MainClass:
	def __init__(self):
		curses.wrapper(self.driver_fn)

	def driver_fn(self, stdscr):
		stdscr.clear()

		drawGrid(stdscr, 6, 7, CELL_WIDTH, CELL_HEIGHT, 6, 5)

		stdscr.refresh()
		stdscr.getch()

if __name__=="__main__":
	MainClass()

# out of bounds of screen error. Look at cell_height and cell_width along with rows and columns
