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
    Entity(model = "cube", color = color.rgb(0.16,0.16,0.16), scale = (7.4, 0.05,200), position = (0,-0.28,0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (-4.75,-0.27, 0))
    Entity(model='cube', color = color.rgb(0.13,0.37,0.13), scale = (2,0.04,200), position = (4.5,-0.27, 0))