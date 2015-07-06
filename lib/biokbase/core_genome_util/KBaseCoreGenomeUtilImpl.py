#BEGIN_HEADER
from pprint import pprint
#END_HEADER


class KBaseCoreGenomeUtil:
    '''
    Module Name:
    KBaseCoreGenomeUtil

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass

    def blast_against_genome(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN blast_against_genome

        returnVal = "some/result/objectRef"

        print("in here")
        pprint(ctx)


        #END blast_against_genome

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method blast_against_genome return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
