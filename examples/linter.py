import requests
from pathlib import Path 
from sys import platform
from os import environ

BASE_DOWNLOAD_URL = "https://download.cobaltstrike.com/download"

class C2Lint:
    def __init__(self, cobaltstrike_license):
        self.cobaltstrike_license = cobaltstrike_license
        
        if not self.cobaltstrike_license:
            self.cobaltstrike_license = environ.get('COBALTSTRIKE_LICENSE')
            
        if not self.cobaltstrike_license:
            raise Exception('Cobaltstrike License not provided')
            
        self.__c2_lint_path = None
        
        # elif platform == "darwin":
        
    def __download_packages(self):
         
        if platform == "linux":
            self.__c2_lint_path = Path("/tmp")
        elif platform == "win32":
            self.__c2_lint_path = Path("%userprofile%\AppData\Local\Temp\Windows\Temp")
            
        post_data = {
            'dlkey': self.cobaltstrike_license
        }
            
        initial_post = requests.post(BASE_DOWNLOAD_URL, data=post_data)
        
c2_lint = C2Lint()