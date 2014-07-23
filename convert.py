# get a whole pmwiki website OR html and transform-it to markdown
# designed to provide a markdown structure able to migrate the website to ikiwiki

import sys
import os
import re
import urllib
import json
import convert_ikiwiki

class Convert:
    valid_types = ['html', 'pmwiki']
    ignore_files = ['.htaccess', '.lastmod', '.flock', '.pageindex']
    
    def __init__(self, conf_file, options=''):
        
        # set configurations
        self.set_config(conf_file, options)
        
        # try to import pages
        self.__create_pages()
        self.__update_links()
        
        # execute options
        if self.config['ikiwiki'] == 'True':
            print "-----------------"
            print 'configure ikiwiki'
            self.__post_ikiwiki()
    
    
    def set_config(self, conf_file, options):
        print "---------------------------------"
        print 'set_config('+ conf_file + '/' + options + ')'
        
        # try to open config file
        try:
            f = open(conf_file, 'r')
        except f.DoesNotExists:
            print 'The file <' + conf_file + '> don\'t exists, exiting!'
        
        # try to load json data
        try:
            config = json.loads(f.read())
        except UnboundLocalError:
            print "Invalid configuration file"
            return False
    
        self.config = config
        self.config['url_append'] = ''
        if (self.config['source_type'] in self.valid_types):
            # TODO: python - como fazer uma chamada dinamica de funcao a partir de uma string?
            #func_name = '__set_type_' + config['source_type']
            #getattr(self, func_name)(*args)
            if (self.config['source_type'] == 'html'):
                self.__set_type_html()
            elif (self.config['source_type'] == 'pmwiki'):
                self.__set_type_pmwiki()
        
        return True

    
    def __create_pages(self):
        print "----------------"
        print '__create pages()'
        
        for page in os.listdir(self.config['source_dir']):
            if page not in self.ignore_files:
                dst = self.config['output'] + '/' + page + '.mdwn'
                url = self.config['source_address'] + '/' + self.config['url_append'] + page
                if self.config['source_type'] == 'pmwiki':
                    url += '?action=markdown'
                    self.__download_page(url, dst)
                    
        return True    
    
    def __download_page(self, url, dst):
        try:
            image_dwl = urllib.urlopen(url)
        except HTTPError, e:
            print e.code
            print url
            return False
        except URLError, e:
            print e.reason
            print url
            return False
        print dst
        f = open(dst, "w")
        f.write(image_dwl.read())
        f.close()
        return True
    
    def __update_links(self):
        print '--------------'
        print 'update_links()'
        address_src = self.config['source_address'].replace('/', '\/') + '\/index.php?n='
        address_replace = self.config['output_address'].replace('/', '\/') + '\/'
        
        cmd = "find '" + self.config['output'] + "' -type f -exec sed -i 's/" + address_src + "/" + address_replace + "/g' {} \;"
        print cmd
        os.system(cmd)
        
        return True

    def __ikikiwi_config(self):
        print "----------------"
        print 'ikiwiki_config()'
        # do ...
        return True


    # HTML specific
    def __set_type_html(self):
        print "----------------"
        print '__set_type_html()'
        
        # include if exists extra class 
        
        return True
    
    # PMWIKI specific
    def __set_type_pmwiki(self):
        print "----------------"
        print '__set_type_pmwiki()'
        self.config['source_dir'] += '/wiki.d'
        self.config['url_append'] = 'index.php?n='

        # include if exists extra class 
        
        return True
    
    def __post_ikiwiki(self):
        print "----------------"
        print "__post_ikiwiki()"
        return True


conf_file = sys.argv[1]
convert = Convert(conf_file)
