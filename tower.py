from enum import Enum, auto

# class Tower_Status(Enum):
#     READY = auto()
#     FIRING = auto()
#     COOLDOWN = auto()

# This should be the 'model'
class TowerModel:
    def __init__(self, attack_range: float, damage: int, attack_speed: int, effects):
        self.effects = [] # Fix Later
        self.damage = damage
        self.attack_range = attack_range
        self.atk_cd = attack_speed
        self.atk_timer = 0

