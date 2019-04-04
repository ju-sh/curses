import curses

class MainClass:
	def __init__(self):
		#curses.wrapper() does the following:
		#  Before calling its argument function:-
		#   - Initializes curses
		#   - Turns off echo
		#   - Enables cbreak mode (no need to press enter)
		#   - Enables keypad mode (curses will process special keys like PAGE_DOWN and navigation keys)

		#  After execution of its argument function:-
		#   - Disables keypad mode
		#   - Disables cbreak mode
		#   - Turns on echo
		#   - Shuts down curses and restores cooked mode of terminal
		curses.wrapper(self.driver_fn)

	def driver_fn(self, stdscr):
		pass

if __name__=="__main__":
	MainClass()
