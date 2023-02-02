## Font management class

from typing import Dict, List
import pygame
import config
import scenes
from scenes.scene import Scene

def get_scene_cls(name: str):
    if name not in scenes.SCENES:
        raise Exception("Scene Not Found!")
    return scenes.SCENES[name]

class SceneManager(object):

    _instance = None
    # scenes: Dict[str, Scene] = {}
    # scene_stack: List[Scene] = []
    active_scene: Scene = None
    display: pygame.surface.Surface

    def __init__(self, display: pygame.surface.Surface):

        # for k in scenes.SCENES:
        #     self.scenes[k] = scenes.SCENES[k](display)

        self.display = display

        self.load_scene(config.START_SCENE)


    def __new__(cls, display: pygame.surface.Surface):
        if cls._instance is None:
            
            print("Creating SceneManager class!")
            cls._instance = super(SceneManager, cls).__new__(cls)

        return cls._instance

    def load_scene(self, name: str):

        if self.active_scene is not None:
            self.active_scene.cleanup()

        cls = get_scene_cls(name)
        scene = cls(self.display)
        scene.setup()
        self.active_scene = scene

    def get_active(self):

        return self.active_scene

