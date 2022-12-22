from enum import Enum


class CartStatus(Enum):
    deactivate = 0
    activate = 1


class OrderStatus(Enum):
    deactivate = 0
    notPaid = 1
    paid = 2
    shipping = 3


class ProductStatus(Enum):
    deactivate = 0
    activate = 1


class UserStatus(Enum):
    deactivate = 0
    activate = 1


class ProductCategory(Enum):
    KEYBOARD = 0
    EARPHONE = 1
    MOUSE = 2
    DESKTOP = 3


@staticmethod
def list():
    return list(map(lambda c: c.value, ProductCategory))


@staticmethod
def dict():
    return [
        {"category": "鍵盤", "value": ProductCategory.KEYBOARD.value},
        {"category": "耳機", "value": ProductCategory.EARPHONE.value},
        {"category": "滑鼠", "value": ProductCategory.MOUSE.value},
        {"category": "桌機", "value": ProductCategory.DESKTOP.value}
    ]


if __name__ == '__main__':
    print(UserStatus.deactivate.value)
