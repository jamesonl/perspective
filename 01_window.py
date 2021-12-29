from direct.task import Task
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile

loadPrcFile("config/conf.prc")

class MyGame(ShowBase):
    """docstring for MyGame."""

    def __init__(self):
        super().__init__()

        scene = self.loader.loadModel("models/environment")
        scene.reparentTo(self.render)
        scene.setScale(0.25, 0.25, 0.25)
        scene.setPos(-8, 42, 0)

        box = self.loader.loadModel("models/box")
        box.setPos(0, 10, 0)
        box.reparentTo(self.render)

        panda = self.loader.loadModel("models/panda")
        panda.setPos(-2, 10, 0)
        panda.setScale(0.2, 0.2, 0.2)
        panda.reparentTo(self.render)





game = MyGame()

print(camera)

game.run()
