import requests
import re
import os

from pathlib import Path 
from sys import platform


BASE_TOKEN_URL = "https://download.cobaltstrike.com/download"
BASE_DOWNLOAD_URL = "https://download.cobaltstrike.com"

PACKAGES = {
    "win32": "cobaltstrike-dist.zip",
    "darwin": "cobaltstrike-dist.dmg",
    "linux": "cobaltstrike-dist.tgz"
}


class C2Lint:
    def __init__(self, cobaltstrike_license=None):
        self.cobaltstrike_license = cobaltstrike_license
        
        if not self.cobaltstrike_license:
            self.cobaltstrike_license = os.environ.get('COBALTSTRIKE_LICENSE')
            
        if not self.cobaltstrike_license:
            raise Exception('Cobaltstrike License not provided')
            
        self.__c2_lint_path = None
        
        # Now get the linter
        self.__download_packages()
        
        # elif platform == "darwin":
        
    def __download_packages(self):
        
        post_data = {
            'dlkey': self.cobaltstrike_license
        }
        
        initial_post = requests.post(BASE_TOKEN_URL, data=post_data)
        token = re.findall(r'\/downloads\/[0-9a-zA-Z]{0,}\/latest46', initial_post.text)
        
        print(token)
         
        
            
        if platform == "win32":
            
            self.__c2_lint_path = Path("%userprofile%\AppData\Local\Temp\Windows\Temp")
        elif platform == "darwin":
            
            self.__c2_lint_path = Path("/tmp")
        elif platform == "linux":
            
            self.__c2_lint_path = Path("/tmp")
        else:
            raise Exception()
            
        self.__c2_lint_path.mkdir('cobaltstrike')
        

        
    def lint(self):
        testingoutput = os.popen('cd ' + randomize_settings['cobalt'] + ' && ' + randomize_settings['cobalt'] + 'c2lint ' + randomize_settings['tempfilename']).readlines()
        fail = False
        for outputline in testingoutput:
            if 'Error(s)' in outputline or '[-]' in outputline:
                fail = True
            if fail and processdetails['errorcount'] < 4:
                print '	[-] Error with c2lint check - Attempt ' + str(processdetails['errorcount']) + ' of 3'
                processdetails['errorcount'] += 1
                c2lint()
            elif fail and processdetails['errorcount'] > 3:
                for _ in testingoutput:
                    print _
                print '[!] The profile failed c2lint error checking three times. Review the c2lint error report above and modify the profile. Exiting.'
                os.system('rm ' + randomize_settings['tempfilename'])
                os._exit(0)
        processdetails['errorcount'] = 1
        return True
        
c2_lint = C2Lint()