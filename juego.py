import sys
class Juego:
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x2 <= x1 <= x2 + bsize:
            if y2 <= y1 <= y2 + bsize:
                return True
        return False

    def salir(self):
        return sys.exit()