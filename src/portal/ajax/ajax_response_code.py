from enum import Enum


class AjaxResponseCode(Enum):
    success = 200
    invalid = 400
    failure = 500
