from secrets import choice
ALLOWED_CHARS: str = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def generate_password(length: int):
    return ''.join([choice(ALLOWED_CHARS) for _ in range(length)])