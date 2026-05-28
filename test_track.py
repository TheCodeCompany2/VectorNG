# ==============================================================================
# Copyright © 2026 TheCodeCompany2. All rights reserved.
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
import math
engine = Ursina()

def build_track():
#straight1
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (7.4, 0.05,200), position = (0,-0.28,0))
#runoffs for straight1 
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (-4.75,-0.27, 0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (4.5,-0.27, 0))
#barriers for straight1
    Entity(model='cube', color = color.rgb(0.475,0.475,0.475), scale = (0.3,0.8,280), position = (-5.75, 0, 0))
    Entity(model='cube', color = color.rgb(0.475,0.475,0.475), scale = (0.3,0.8,200), position = (5, 0, 0))
#hairpin apron(track)
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (36, 0.05, 25), position = (13, -0.28, 107))
#hairpin outside apex kerb turn1
    num_segments = 30
    outer_radius = 18.0
    center_x = 13
    center_z = 101.0

    for i in range(num_segments + 1):
        angle_radians = math.radians((i/num_segments)*180)
        x_pos = center_x + (outer_radius * math.cos(angle_radians))
        z_pos = center_z + (outer_radius * math.sin(angle_radians))
        angle_degrees = 90 - math.degrees(angle_radians)

        Entity(
            model = "cube", 
            color = color.rgb(0.5,0.5, 0.5) if i%2 ==0 else color.rgb(0.8,0.1,0.1),
            scale = (1.5,0.01,3.8),
            position= (x_pos, -0.2, z_pos),
            rotation_y=angle_degrees
        )
#gravel trap for outside turn1
    num_segments = 30
    gravel_radius = 19.5
    center_x = 12.5
    center_z = 101.0

    for i in range(num_segments + 1):
        angle_radians = math.radians((i/num_segments)*180)
        x_pos = center_x + (gravel_radius * math.cos(angle_radians))
        z_pos = center_z + (gravel_radius * math.sin(angle_radians))
        angle_degrees = 90 - math.degrees(angle_radians)

        Entity(
            model = "cube", 
            color = color.rgb(0.78,0.72,0.61),
            scale = (4.5,0.01,4),
            position= (x_pos, -0.22, z_pos),
            rotation_y=angle_degrees
        )
#barriers for turn1
    Entity(model='cube', color = color.rgb(0.475,0.475,0.475), scale = (36,0.8,0.3), position = (13,0,140))
#straight2
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (7.4, 0.05,200), position = (25,-0.28,0))
#runoffs for straight2
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (20.25,-0.27, 0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (29.25,-0.27, 0))
#barriers for straight2
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,200), position = (19.25, 0, 0))
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,280), position = (30.75, 0, 0))