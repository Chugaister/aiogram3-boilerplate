
class APIError(Exception):

    def __init__(self, status_code: int, json: dict):
        super().__init__(f"{status_code} {json}")
        self.status_code = status_code
        self.json = json


class BadRequestError(APIError):
    pass


class NotFoundError(APIError):
    pass


class UnauthorizedError(APIError):
    pass


class UnprocessableEntity(APIError):
    pass


def exception_factory(status_code: int, json: dict):
    if status_code == 400:
        return BadRequestError(status_code, json)
    if status_code == 401:
        return UnauthorizedError(status_code, json)
    if status_code == 404:
        return NotFoundError(status_code, json)
    if status_code == 422:
        return UnprocessableEntity(status_code, json)
    else:
        return APIError(status_code, json)
