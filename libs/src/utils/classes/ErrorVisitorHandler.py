class ErrorVisitorHandler:
    def __init__(self):
        self.errors = []

    def report_error(self, line, column, message):
        error_msg = f"Error: at line {line}:{column}: {message}"
        self.errors.append(error_msg)
        return error_msg

    def get_errors(self):
        return self.errors

    def clear_errors(self):
        self.errors = []
