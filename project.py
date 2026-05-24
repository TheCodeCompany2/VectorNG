# ==============================================================================
# Copyright (c) 2026 TheCodeCompany2. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from ursina import *
engine = Ursina()

car = Entity(model = 'cube', color=color.rgb(0, 0, 64), scale=(1.2, 0.5, 3))
car.wireframe_setter = True

nose = Entity(parent = car, model = "cube", color = color.rgb(204, 0, 0), scale = (1.8, 0.1, 0.5), z = 1.7, y = 0.1)

tail = Entity(parent = car, model = "cube", color = color.rgb(0, 0, 0), scale = (1.4, 0.6, 0.1), z = -1.5, y = 0.4)

airbox = Entity(parent = car, model = "cube", color = color.rgb(255, 222, 0), scale = (0.3, 0.5, 0.4), z = -0.2, y = 0.5)

camera.parent = car
camera.position = (0, 4.5,-15)
camera.rotation_x = 10

def update():
    current_speed = 0
    if held_keys['space']:
       current_speed = 50
    else:
        current_speed = 10    
    
    if held_keys['w']:
        car.z += current_speed * time.dt
    elif held_keys['s']:
        car.z -= current_speed * time.dt
    
    if held_keys['a']:
        car.x -= current_speed * time.dt
    elif held_keys['d']:
        car.x += current_speed * time.dt
 
engine.run()
