
# petlink - Decode and encode PETlink streams. 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 

__all__ = ['petlink32_info','petlink32_bin_addresses']

from simplewrap import *
import os

class ErrorInCFunction(Exception): 
    def __init__(self,msg,status,function_name): 
        self.msg = str(msg) 
        self.status = status
        self.function_name = function_name
        if self.status == status_io_error(): 
            self.status_msg = "IO Error"
        elif self.status == status_decode_error(): 
            self.status_msg = "Error Decoding file content"
        else: 
            self.status_msg = "Unspecified Error"
    def __str__(self): 
        return "'%s' returned by the C Function '%s'. %s"%(self.status_msg,self.function_name,self.msg)


# Load library
petlink32_c = load_c_library("petlink32_c",localpath())

# Utility functions 
def status_success(): 
    """Returns the value returned by the function calls to the library in case of success. """
    r = call_c_function( petlink32_c.status_success, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value

def status_io_error(): 
    """Returns the integer value returned by the function calls to the library in case of IO error. """
    r = call_c_function( petlink32_c.status_io_error, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value

def status_decode_error(): 
    """Returns the value returned by the function calls to the library in case of error decoding a file. """
    r = call_c_function( petlink32_c.status_decode_error, [{'name':'return_value',  'type':'int', 'value':None}] ) 
    return r.return_value


# Create interface to the C functions: 
def test_library_petlink32_c(): 
    """Test whether the C library petlink32_c responds. """
    number = 101 # just a number
    descriptor = [  {'name':'input',  'type':'int', 'value':number},
                    {'name':'output', 'type':'int', 'value':None },  ]
    r = call_c_function( petlink32_c.echo, descriptor ) 
    return r.output == number


def petlink32_info(filename,n_packets): 
    """Extracts summary information from a listmode binary file. """ 
    descriptor = [  {'name':'filename',    'type':'string', 'value':filename ,'size':len(filename)},
                    {'name':'n_packets',    'type':'int',    'value':n_packets  },
                    {'name':'n_prompts',   'type':'int',    'value':None      },
                    {'name':'n_delayed',   'type':'int',    'value':None      },
                    {'name':'n_tags',      'type':'int',    'value':None      },
                    {'name':'n_time',      'type':'int',    'value':None      }, 
                    {'name':'n_motion',    'type':'int',    'value':None      }, 
                    {'name':'n_monitoring','type':'int',    'value':None      }, 
                    {'name':'n_control',   'type':'int',    'value':None      },  ] 
    r = call_c_function( petlink32_c.petlink32_info, descriptor ) 
    if not r.status == status_success(): 
        raise ErrorInCFunction("The execution of petlink32_info was unsuccesful.",r.status,'petlink32_c.petlink32_info')
    return r.dictionary 


def petlink32_bin_addresses(filename,n_packets): 
    """Extract list of bin indexes from listmode data. """ 
    descriptor = [  {'name':'filename',     'type':'string', 'value':filename ,'size':len(filename)},
                    {'name':'n_packets',     'type':'int',    'value':n_packets      }, 
                    {'name':'bin_addresses','type':'array',  'value':None, 'dtype':int32, 'size':(1,n_packets)},
                    {'name':'n_prompts',    'type':'int',    'value':None      }, 
                    {'name':'n_delayed',    'type':'int',    'value':None      }, 
                    {'name':'n_tags',       'type':'int',    'value':None      }, 
                    {'name':'n_time',       'type':'int',    'value':None      }, 
                    {'name':'n_motion',     'type':'int',    'value':None      }, 
                    {'name':'n_monitoring', 'type':'int',    'value':None      }, 
                    {'name':'n_control',    'type':'int',    'value':None      },  ] 
    r = call_c_function( petlink32_c.petlink32_bin_addresses, descriptor ) 
    if not r.status == status_success(): 
        raise ErrorInCFunction("The execution of petlink32_bin_addresses was unsuccesful.",r.status,'petlink32_c.petlink32_bin_addresses')
    return r.dictionary 







