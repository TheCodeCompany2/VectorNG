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
engine = Ursina()

def build_track():
#straight1
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (7.4, 0.05,200), position = (0,-0.28,0))
#runoffs for straight1 
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (-4.75,-0.27, 0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (4.5,-0.27, 0))
#barriers for straight1
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,200), position = (-5.75, 0, 0))
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,200), position = (5, 0, 0))
#hairpin apron(track)
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (36, 0.05, 25), position = (13, -0.28, 107))
#hairpin inside apex kerb
    Entity(model = "sphere", color = color.rgb(0.9,0.1,0.1), scale = (14, 0.08, 20), position = (12.25, -0.2, 98))
#straight2
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (7.4, 0.05,200), position = (25,-0.28,0))
#runoffs for straight2
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (20.25,-0.27, 0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (29.25,-0.27, 0))
#barriers for straight2
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,200), position = (19.25, 0, 0))
    Entity(model='cube', color = color.rgb(0.5,0.5,0.5), scale = (0.3,0.8,200), position = (30.75, 0, 0))