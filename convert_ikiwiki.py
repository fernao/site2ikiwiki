# execute tasks for creating ikiwiki install by hand
# follow: http://ikiwiki.info/setup/byhand/


import sys
import os
import re
import urllib
import json

class ConvertIkiwiki:

    def __init__(self, conf):
        print "CreateIkiwiki.__init__()"
        self.__set_conf(conf)
        
        sync_ikiwiki()

    def __set_config(self, conf):
        self.config = conf

    def __get_ikiwiki_setup(self):
        return self.config["sitename"] + ".setup"

    def create_ikiwiki(self):
        
        # ikiwiki source
        try:
            os.listdir(self.config["ikiwiki_source"])
        except OSError:
            os.mkdir(self.config["ikiwiki_source"])
            
        try:
            os.listdir(self.config["ikiwiki_dest"])
        except OSError:
            os.mkdir(self.config["ikiwiki_dest"])

        print "----"
        print "Creating ikiwiki instance..."
        cmd = "ikiwiki --verbose " + self.config["ikiwiki_source"] + " " + self.config["ikiwiki_dest"] + " --url=" + self.config["ikiwiki_address"]
        os.system(cmd)
        
        
        return True

    def sync_ikiwiki(self):
        print "sync_ikiwiki()"
        
        cmd = "ikiwiki --setup " + self.__get_ikiwiki_setup()
        print cmd
        os.system(cmd)
        
        return True
