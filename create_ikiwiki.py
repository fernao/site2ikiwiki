# execute tasks for creating ikiwiki install by hand
# follow: http://ikiwiki.info/setup/byhand/


import sys
import os
import re
import urllib
import json

class CreateIkiwiki:

    def __init__(self, conf):
        print "CreateIkiwiki.__init__()"
        self.__set_config(conf)
        
        # create and make it's first sync
        self.create_ikiwiki()
        self.sync_ikiwiki()

    def __set_config(self, conf):
        self.config = conf

    def __get_ikiwiki_setup(self):
        return "~/.ikiwiki/" + self.config["sitename"] + ".setup"

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
        
        print "----"
        print "Creating ikiwiki setup file..."
        
        cmd = "ikiwiki " + self.config["ikiwiki_source"] + " " + self.config["ikiwiki_dest"] + " --url=" + self.config["ikiwiki_address"] + " --dumpsetup " + self.__get_ikiwiki_setup()
        os.system(cmd)
        
        print "----"
        print "Creating version system on your new ikiwiki..."
        version_control_folder = self.config["ikiwiki_source"] + "." + self.config["ikiwiki_version_control"]
        try:
            os.listdir(version_control_folder)
        except OSError:
            os.mkdir(version_control_folder)
        cmd = "ikiwiki-makerepo " + self.config["ikiwiki_version_control"] + " " + self.config["ikiwiki_source"] + " " + version_control_folder
        os.system(cmd)

        return True
    
    def ikiwiki_conf_defaults(self):
        ''' 
        sets some defaults to setup file
        '''
        return True


    def sync_ikiwiki(self):
        print "sync_ikiwiki()"
        
        cmd = "ikiwiki --setup " + self.__get_ikiwiki_setup()
        print cmd
        os.system(cmd)
        
        return True
