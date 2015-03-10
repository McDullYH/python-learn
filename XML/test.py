#!/usr/bin/python


# import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup as bs
from bs4.element import Tag
import sys
import re

class XMLConfiguratorB():
    def __init__(self,file_path=None):
        if file_path==None:
            pass
        self.file_path=file_path
        self.tree = ET.parse(file_path)
        self.root = tree.getroot()
    def setProperty(self,name,value):
        if type(name)!=str or type(value)!=str:
            print 'key and value must be str'
            return False
        ele=root.find(name)
        if ele==None:
            configuration_tag=root.find('configuration')
            property_tag=ET.SubElement(configuration_tag,'property')
            name_tag=ET.SubElement(property_tag,name)
            value_tag=ET.SubElement(property_tag,value)
            tree.write('output.xml')
        else:
            pass
        return True


class XMLConfigurator():
    def __init__(self,file_path=None):
        if file_path==None:
            pass
        with open(file_path,'r') as f:
            self.soup=bs(f.read(),"xml")
        self.file_path=file_path
    def setProperty(self,name,value):
        if type(name)!=str or type(value)!=str:
            print 'key and value must be str'
            return False
        if not verify(name,value):
            return False
        ele=self.soup.find(name='name',text=name)
        if ele==None:
            print "create it"
            p=Tag(name='property')
            n=Tag(name='name')
            n.string=name
            v=Tag(name='value')
            v.string=value
            p.append(n)
            p.append(v)
            configuration_tag=self.soup.find('configuration')
            configuration_tag.append(p)
        else:
            print "get it"
            ele.parent.find('value').string=value
        return True
    def write(self,output_path='output.xml'):
        with open(output_path,'w') as f:
            f.write(str(self.soup))


class ValidatorError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)

class RETester:
    def __init__(self,re_str,separator=None):
        if type(separator) == str and len(separator)>1:
            raise ValidatorError("seperator must be str and has size of 1")
        self.pattern=re.compile(re_str)
        self.separator=separator
    def set_separator(self,separator):
        if len(separator)>1:
            raise ValidatorError("seperator must be size of 1")
        self.separator=separator
        return self
        
    def __call__(self,source):
        if self.separator:
            for sub in source.split(self.separator):
                if not self.pattern.match(sub):
                    return False
        elif not self.pattern.match(source):
            return False
        return True

# must add $ at end!
boolean=RETester(r'([Tt]rue)$|([Ff]alse)$')
local_path=RETester(r'(\/([\w]+))+$')
file_path=RETester(r'file:\/\/(\/([\w]+))+$')
ip_port=RETester(r'[\w\-]+(:[\d]+)?$')


# use regular exp to validate the value
verifitor={'dfs.client.read.shortcircuit':boolean,
            'dfs.domain.socket.path':local_path,
            'dfs.datanode.data.dir':file_path.set_separator(','),
            'mapreduce.jobhistory.webapp.address':ip_port,
            }




def verify(name,value):
    #return verifitor[name.strip()](value.strip())
    if not verifitor[name.strip()](value.strip()):
        print "property '%s' is not valid for value '%s' "  % (name,value)
    else:
        return True
    
    

if __name__=='__main__':
    c=XMLConfigurator(sys.argv[1])
    c.setProperty(r'dfs.domain.socket.path','domain')
    c.setProperty(r'dfs.domain.socket.path','/domain')
    c.setProperty(r'dfs.datanode.data.dir','file')
    c.setProperty(r'dfs.datanode.data.dir','/file')
    c.setProperty(r'dfs.datanode.data.dir','file:///file,file:///file')
    c.setProperty(r'dfs.datanode.data.dir','file:///file,file:///file/impala-shell')
    c.setProperty(r'dfs.client.read.shortcircuit','FF')
    c.setProperty(r'dfs.client.read.shortcircuit','Flse')
    c.setProperty(r'dfs.client.read.shortcircuit','False')
    c.setProperty(r'dfs.client.read.shortcircuit','True')
    c.setProperty(r'mapreduce.jobhistory.webapp.address',':8080')
    c.setProperty(r'mapreduce.jobhistory.webapp.address','impala-server1:')
    c.setProperty(r'mapreduce.jobhistory.webapp.address','impala-server1')
    c.setProperty(r'mapreduce.jobhistory.webapp.address','impala-server1:8080')
    c.write()

    

