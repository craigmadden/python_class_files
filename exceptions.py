class InvalidUsernameError(Exception):
    pass

def is_valid_username(username):
    if len(username) > 10:
        raise InvalidUsernameError("Name too large")

try:
    is_valid_username("joe")
    # lots of other code ....

except InvalidUsernameError as e:
    # e is the exception the thing that caused the exception
    # handle error here
    print e.args