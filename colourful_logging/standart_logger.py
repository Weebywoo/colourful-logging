from datetime import datetime
from typing import Optional
import time


# class Colours:
#     GREEN: str = '\u001b[32m'
#     YELLOW: str = '\u001b[33m'
#     ORANGE: str = ''
#     RED: str = '\u001b[31m'
#     WHITE: str = '\u001b[37m'


class Logger:

    @classmethod
    def ExceptionLogger(cls, severity: Optional[int] = 3):
        """ExceptionLogger should only be used as a decorator.

        Keyword arguments:
        severity -- declares the severity of reported issues of decorated function

        Valid severities:
        LOW -- green
        MEDIUM -- yellow severity
        WARNING -- orange severity
        ERROR -- red, high severity
        """

        def wrapper(func):

            def wrapped_func(*args):
                try:
                    func(*args)

                except Exception as exception:
                    if severity == 0:
                        cls.logException(exception, 'GREEN')

                    elif severity == 1:
                        cls.logException(exception, 'YELLOW')

                    elif severity == 2:
                        cls.logException(exception, 'ORANGE')

                    elif severity == 3:
                        cls.logException(exception, 'RED')

            return wrapped_func

        return wrapper

    @staticmethod
    def logException(exception: Exception, colour: str) -> None:
        timestamp = datetime.fromtimestamp(time.time())

        print(
            f"{timestamp} {exception.ljust(10, ' ')}: {exception.__cause__}"
        )
