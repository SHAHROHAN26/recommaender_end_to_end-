import os
import sys

class InsuranceException(Exception):

    def __init__(self,error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message,error_detail=error_detail)

    @staticmethod
    def error_message_detail(error_message:Exception,error_detail:sys)->str:
        _,_, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_frame.f_lineno

        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message=f"error occuraed in python script name[{file_name}]" \
                        f"line number[{exc_tb.tb_lineno}] error message]."

        return error_message
    
    def __repr__(self):
        return InsuranceException.__name__.__str__()

    def __str__(self):
        return self.error_message