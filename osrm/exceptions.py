

class Timeout(BaseException):
    def __init__(self):
        pass


class HTTPError(BaseException):
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f"status: {self.status}"


class RequestError(BaseException):
    def __init__(self, exception):
        self.exception = exception

    def __str__(self):
        return f"{self.exception}"