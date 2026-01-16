import sys
import select
import termios
import tty

class keyboard_setup:
    def __enter__(self):
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        return self

    def __exit__(self, type, value, traceback):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def get_input(self):
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            char = sys.stdin.read(1)

            if char == '\x1b':
                seq = sys.stdin.read(2)
                if seq == '[A': return "HAUT"
                if seq == '[B': return "BAS"
                if seq == '[C': return "DROITE"
                if seq == '[D': return "GAUCHE"

            return char
        return None
