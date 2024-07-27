
import sys

class CustomException(Exception):
    def __init__(self, error_message,error_details:sys) -> None:
        self.error_message = error_message
        self.error_details = error_details

        _,_,exc_tb= self.error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

        self.error_message = "Error occurred in script [{0}] in line [{1}] error message [{2}]".format(self.file_name,self.lineno,self.error_message)

    def __str__(self) -> str:
        return self.error_message
