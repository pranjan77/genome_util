#BEGIN_HEADER

import sys
import os
import glob
import json
from pprint import pprint
#sys.path.insert(0, '/kb/dev_container/modules/genome_util/lib/biokbase/genome_util')
import script_util
#from biokbase.workspace.client import Workspace
#from workspace.client import Workspace


#END_HEADER


class KBaseGenomeUtil:
    '''
    Module Name:
    KBaseGenomeUtil

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    # Config variables that SHOULD get overwritten in the constructor
    __TEMP_DIR = 'temp_dir'
    __WS_URL = 'https://kbase.us/services/ws'
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR

        # This is where config variable for deploy.cfg are available
        print "SCRIPT CONFIG:"
        pprint(config)
        if 'ws_url' in config:
        	__WS_URL = config['ws_url']
        	print "Setting __WS_URL = "+__WS_URL
        if 'temp_dir' in config:
        	__TEMP_DIR = config['temp_dir']
        	print "Setting __TEMP_DIR = "+__TEMP_DIR

        #END_CONSTRUCTOR
        pass

    def blast_against_genome(self, ctx, params):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN blast_against_genome
	
	print "start"
	if len(params['query']) > 5:
		sequence=params['query']
	else:
		#error message: your sequence are too short
		raise Exception("The input sequence is too short!")
	#else:
		#sequence=script_util.get_seq(params['gene_id'])
		#sequence=(params['gene_id'])
	

	genome_id='Bifidobacterium_animalis_subsp._lactis_AD011'
	workspaceid='plane83:1436884411390'
	
	#print "generate input file for query sequence\n"
	target=open('tmp_seq','w')
	target.write(">")
	target.write("input_seq\n")
	target.write(sequence)
	target.close()
	

	#print "downloading genome object from workspace\n"
	#genome=script_util.get_genome('genome_id','workspaceid',ctx['token'])
	#print "finished downloading\n";

	if os.path.exists('blast_db'):
		files=glob.glob('blast_db/*')
		for f in files: os.remove(f)
	if not os.path.exists('blast_db'): os.makedirs('blast_db')
	#with open('tmp_data','w') as outfile:
	#	json.dump(genome, outfile)	
	

	check_seq=0
	if(params['blast_program'] == 'blastp'):
		formatdb_type='T'
		#extract protein sequences from the genome object
		res1=open('tmp_data').read()
		res=json.loads(res1)
		target=open('blast_db/tmp_genome_fasta','w')
		for gene in res['data']['features']:
			if 'protein_translation' in gene.keys():
				target.write(">" + gene['id'] + "\n" + gene['protein_translation'] + "\n")
				check_seq=1
		target.close()
	
	
	if(params['blast_program'] == 'blastn'):
		formatdb_type='F'
		#extract dna sequence from the genome object
		res1=open('tmp_data').read()
		res=json.loads(res1)
		target=open('blast_db/tmp_genome_fasta','w')
		for gene in res['data']['features']:
			if 'dna_sequence' in gene.keys():
				target.write(">" + gene['id'] + "\n" + gene['dna_sequence'] + "\n")
				check_seq=1
		target.close()

	if check_seq == 0:
		raise Exception("The genome object does not contain any sequences!")
	
	
	
	#os.remove('tmp_data')
	
	#print "formatdb..\n"
	#format database for blast
	
	cmdstring="formatdb -i blast_db/tmp_genome_fasta -p %s" %(formatdb_type)
	os.system(cmdstring)

	#blast search
	cmdstring="blastall -p %s -i tmp_seq -m 9 -o tmp_out -d blast_db/tmp_genome_fasta -e %s" % (params['blast_program'], params['e-value'])
	os.system(cmdstring)
	os.remove('tmp_seq')
	
	#extract the blast output
	res=script_util.extract_blast_output('tmp_out')
	os.remove('tmp_out')
	res1=json.loads(res)
	
	print "finished"
	returnVal = res1
        #END blast_against_genome

        # At some point might do deeper type checking...
        if not isinstance(returnVal, list):
            raise ValueError('Method blast_against_genome return value ' +
                             'returnVal is not type list as required.')
        # return the results
        return [returnVal]

    def compare_genome_groups(self, ctx, input):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN compare_genome_groups
        #END compare_genome_groups

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method compare_genome_groups return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
