from typing import Dict

from scenes.scene import Scene
from .game_scene import GameScene
from .menu_scene import MenuScene
from .pause_game_scene import PauseGameScene

MENU_SCENE = "MENU"
GAME_SCENE = "GAME"
PAUSE_GAME_SCENE = "PAUSE_GAME"

SCENES: Dict[str, type[Scene]] = {
    MENU_SCENE: MenuScene,
    GAME_SCENE: GameScene,
    PAUSE_GAME_SCENE: PauseGameScene
}

def get_scene_cls(name: str):
    if name not in SCENES:
        raise Exception("Scene Not Found!")
    return SCENES[name]