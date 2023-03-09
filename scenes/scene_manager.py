# Font management class
import pygame


class SceneManager(object):

    _instance = None

    scene_stack = []

    # scenes: Dict[str, Scene] = {}
    # scene_stack: List[Scene] = []
    # active_scene: Scene = None

    def __init__(self):

        # for k in scenes.SCENES:
        #     self.scenes[k] = scenes.SCENES[k](display)

        pass

    def __new__(cls):
        if cls._instance is None:

            print("Creating SceneManager class!")
            cls._instance = super(SceneManager, cls).__new__(cls)

        return cls._instance

    def push(self, scene):

        if len(self.scene_stack) > 0:
            self.scene_stack[-1].osbcuring()

        self.scene_stack.append(scene)
        self.scene_stack[-1].setup()

    def pop(self):

        if len(self.scene_stack) <= 0:
            return

        remove_scene = self.scene_stack.pop()
        remove_scene.cleanup()

        if len(self.scene_stack) > 0:
            self.scene_stack[-1].revealed()

    def handle_event(self, event):

        for scene in reversed(self.scene_stack):
            if scene.handle_event(event):
                break

    def update(self, dt):

        for scene in reversed(self.scene_stack):
            scene.update(dt)

    def render(self, display: pygame.surface.Surface):

        for scene in self.scene_stack:
            scene.render(display)
