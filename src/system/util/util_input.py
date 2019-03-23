import hashlib
import uuid


def input_format(input_str: any) -> str:
    input_str = input_str if isinstance(input_str, str) else ''
    input_str = input_str.replace(' ', '')
    return input_str


def input_match(input_a: str, input_b: str) -> bool:
    return input_a == input_b


def input_hash(input_str: str) -> str:
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + input_str.encode()).hexdigest() + ':' + salt


def input_match_hash(input_str: str, input_str_hashed: str) -> bool:
    password, salt = input_str_hashed.split(':')
    return password == hashlib.sha256(salt.encode() + input_str.encode()).hexdigest()
