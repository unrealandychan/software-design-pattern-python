# This is from the video: https://youtu.be/1ZM88C_CLDY?si=AIrxK4qmX0MoFYI0

# Single Responsibility Principle
# A class should have only one reason to change
# Wrong Example

class AuthService:
    logfile = 'log.txt'

    def login(self, username, password):
        if self._check_password(username, password):
            self._log('login successful')
            return True
        else:
            self._log('login failed')
            return False

    def _check_password(self, username, password):
        if username == 'tim' and password == 'password':
            return True
        return False

    def _log(self, message):
        with open(self.logfile, 'a') as file:
            file.write(message + '\n')


## Right Example
class Logger:
    def log(self, message):
        with open('log.txt', 'a') as file:
            file.write(message + '\n')


class AuthServiceNew:

    def __init__(self, logger: Logger):
        self.logger = logger

    def login(self, username, password):
        if self._check_password(username, password):
            self.logger.log('login successful')
            return True
        return False

    def _check_password(self, username, password):
        if username == 'tim' and password == 'password':
            return True
        return False


logger = Logger()
auth = AuthServiceNew(logger)
auth.login('tim', 'password')
