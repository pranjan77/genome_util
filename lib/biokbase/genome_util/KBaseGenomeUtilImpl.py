#BEGIN_HEADER

import sys
import os
import glob
import json
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
	
	
	if len(params['query']) > 5:
		sequence=params['query']
	else:
		#error message: your sequence are too short
		print "error"
	#else:
		#sequence=script_util.get_seq(params['gene_id'])
		#sequence=(params['gene_id'])
	

	genome_id='Bifidobacterium_animalis_subsp._lactis_AD011'
	workspaceid='plane83:1436884411390'
	
	#print "generate input file\n"
	target=open('tmp_seq','w')
	target.write(">")
	target.write("input_seq\n")
	target.write(sequence)
	target.close()
	
	#print "downloading genome object from workspace\n"
	genome=script_util.get_genome('genome_id','workspaceid',ctx['token'])
	#print "finished downloading\n";
	
	#extract sequences from the genome object
	with open('tmp_data','w') as outfile:
		json.dump(genome, outfile)	
	res1=open('tmp_data').read()
	res=json.loads(res1)
	os.remove('tmp_data')
	#print "making dir\n"
	if os.path.exists('blast_db'):
		files=glob.glob('blast_db/*')
		for f in files: os.remove(f)
	if not os.path.exists('blast_db'): os.makedirs('blast_db')
	target=open('blast_db/tmp_genome_fasta','w')
	for gene in res['data']['features']:
		if 'protein_translation' in gene.keys():
			target.write(">")
			target.write(gene['id'])
			target.write("\n")
			target.write(gene['protein_translation'])
			target.write("\n")
	target.close()
	
	#print "formatdb..\n"
	#format database for blast
	os.system("formatdb -i blast_db/tmp_genome_fasta -p T")
	os.system("blastall -p blastp -i tmp_seq -m 9 -o tmp_out -d blast_db/tmp_genome_fasta")
	os.remove('tmp_seq')

	print "test"
	res=script_util.extract_blast_output('tmp_out')
	os.remove(tmp_out)
	os.remove(input_seq)
	
		
	

	returnVal = res
        #END blast_against_genome

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method blast_against_genome return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
