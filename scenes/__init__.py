from typing import Dict

from scenes.scene import Scene
from .game_scene import GameScene
from .menu_scene import MenuScene

SCENES: Dict[str, type[Scene]] = {
    MenuScene.name: MenuScene,
    GameScene.name: GameScene
}