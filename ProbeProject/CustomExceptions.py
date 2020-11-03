from Error import Error

class IncorrectJSONLoadException(Error):
    """
    Exception raised when a JSON isn't referred as a string depicting the path to the file (e.g., if it were to be
    given as an IOWrapper
    """

    def __init__(self, value, message="A JSON file must be given in a string, not in any other form or wrapper"):
        self.value = value
        self.message = message
        super().__init__(self.message)

class WrongFormatString(Error):
    """
    Exception raised when a parameter which is to be given as a String is given as anything else
    """

    def __init__(self, parametername, value, message=" value must be a String and not anything else"):
        self.value = value
        self.message = f"{parametername} {message}"
        super().__init__(self.message)

class WrongFormatInt(Error):
    """
    Exception raised when a parameter which is to be given as an Int is given as anything else
    """

    def __init__(self, parametername, value, message="Referred value must be given as an Int and not as anything else"):
        self.value = value
        self.message = f"{parametername} {message}"
        super().__init__(self.message)

class UndefinedThresholdError(Error):
    """
    Exception raised when a number doesn't have a threshold to belong to
    """
    def __init__(self, value, message="That value belongs to an unspecified threshold"):
        self.value = value
        self.message = message
        super().__init__(self.message)