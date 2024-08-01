import pygame as pg 
import sys

WIDTH = 640
HEIGHT = 640 
FPS = 60 

class App:
    def __init__(self) -> None:
        pg.init()
        self.screen: pg.display = pg.display.set_mode((WIDTH, HEIGHT))
        self.display: pg.Surface = pg.Surface((WIDTH, HEIGHT))
        self.dt: float = 0
        self.clock: pg.time = pg.time.Clock()

    def render(self):
        self.display.fill((0,0,0))

        # --------- MAIN RENDER ACTIONS ---------- #

        # CODE HERE 

        # ---------------------------------------- #

        self.screen.blit(self.display, (0, 0))
        pg.display.flip()
        pg.display.update()

    def update(self):
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')
        self.dt = self.clock.tick(FPS)
        self.dt /= 1000

    def check_inputs(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if e.type == pg.KEYDOWN:
                if e.key == pg.K_1:
                    pg.quit()
                    sys.exit()
    def run(self):
        while True:
            self.check_inputs()
            self.render()
            self.update()


if __name__ == '__main__':
    app = App()
    app.run()
