from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from numpy import floor

app = Ursina()

window.color = color.rgb(0, 200, 211)
window.exit_button.visible = False

def input(key):
    if key == 'q' or key == 'escape':
        quit()




def update():
    # jeff.rotation_y +=0.3
    # jeff.rotation_x += 0.7
    pass


terrain = Entity(model=None, Collider=None)

terrain_width = 10
for i in range(terrain_width*terrain_width):
    bud = Entity(model='cube', color=color.green)
    
    bud.x = floor(i/terrain_width)
    bud.z = floor(i%terrain_width)
    bud.y = floor(0)
    bud.parent = terrain

terrain.combine()
terrain.collider = 'mesh'
terrain.texture = 'grass_14.png'

subject = FirstPersonController()
subject.x = subject.z = 5
subject.y = 12

app.run()