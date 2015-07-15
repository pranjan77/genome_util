import sys
import os
import json
import re

from biokbase.workspace.client import Workspace


"""
This provides some useful functions for genome_util
By Fei He
"""



#get gene sequences from workspace by gene_id
def get_seq(gene_id):
	seq='proteinsequencesssssssssss'
	return seq



def get_genome(genome_id=None,workspace_id=None,token=None,workspace_url=None):
	#download genome object from workspace
	if workspace_url is None:
		workspace_url='https://kbase.us/services/ws/'
	if token is None:
		with open('/kb/dev_container/modules/genome_util/mytoken.txt') as token_file:
			token=token_file.read()
		token=token.rstrip()


	
	#print token
	#print genome_id
	#print workspace_id
	
	workspace_client=Workspace(url=workspace_url, token=token)
	#genome=workspace_client.get_object({'id':genome_id, 'workspace':workspace_id, 'type':'KBaseGenomes.Genome'})
	genome = workspace_client.get_object({'id' : 'Bifidobacterium_animalis_subsp._lactis_AD011', 'type' : 'KBaseGenomes.Genome',  'workspace' : 'plane83:1436884411390'})
	

	return genome


"""
#res=genome2fasta()
res=open('tmp_genome').read()
res2=json.loads(res)
#with open('tmp_genome2','w') as outfile:
#	json.dump(res2,outfile,indent=4)

#generate fasta file for blast database
target=open('blast_db/tmp_genome_fasta','w')
for gene in res2['data']['features']:
	if 'protein_translation' in gene.keys():
		target.write(">")
		target.write(gene['id'])
		target.write("\n")
		target.write(gene['protein_translation'])
		target.write("\n")
#format database for blast
os.system("formatdb -i blast_db/tmp_genome_fasta -p T")

"""



def extract_blast_output(myfile):
	res=open(myfile).readlines()
	i=0
	info=[]
	for line in res:	
		if re.match(r'^#', line): continue
		line=line.rstrip()
		aa=re.split(r'\t',line)
		tmp={'gene_id':aa[1],'e-value':aa[10],'score':aa[11],'identity':aa[2]}
		info.append(tmp)
	info=json.dumps(info)
	#target=open('tmp_file','w')
	#target.write(info)
	#target.close()
	
	return info






