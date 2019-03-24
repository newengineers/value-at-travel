from flask import jsonify

from portal.ajax.ajax_response_code import AjaxResponseCode


class AjaxResponse:

    def __init__(self, code: AjaxResponseCode, message: str = '', data: dict = None):
        self.code = code
        self.message = message
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: dict):
        if isinstance(data, dict) or data is None:
            self.__data = data or {}
        else:
            raise ValueError('Property "%s" must be of type "%s"' % ('data', 'dict'))

    def send(self) -> str:
        return jsonify(
            {
                'response': self.code.value,
                'message': self.message,
                'data': self.data
            })
