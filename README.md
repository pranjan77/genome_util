

Genome Utilities
===========================

This module provides basic bioinformatic tools for KBase users.


Examples of tools that will be developed in this module:
1) Blast a protein sequence against a genome
2) Generate GeneOntology annotation for a protein sequence, through InterproSCAN.
3) All-aganist-all sequence comparison between two genomes
4) Functional comparison between two genomes





Note for development:\n
1) Delete the PATHONPATH in the 'bin/run_KBaseGenomeUtil.sh'

2) . /kb/dev_container/user-env.sh

3) export PYTHONPATH='kb/deployment/lib'

4) insert 'token=token.rstrip()' in line526 within lib/biokbase/genome_util/KBaseGenomeUtil.py

5) make deploy


6) testing the command:  ./bin/run_KBaseGenomeUtil.sh test/script_test/input.json output.txt /mnt/project/mytoken.txt
