from enum import IntEnum

class Label(IntEnum):
    """Label enumeration for network traffic classification."""
    NORMAL = 0
    DDOS = 1
    BRUTEFORCE = 2
    PORTSCAN = 3
    WEB_ATTACK = 4
