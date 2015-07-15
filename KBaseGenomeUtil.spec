module KBaseGenomeUtil {

    /* @id ws KBaseGenomeUtil.BlastOutput */
    typdef string blast_output_ref;

    /*genome_id is a KBase genome object id*/
    typedef string genome_id;

    
    typedef structure {
    	
	/*only one parameter from query and gene_id is required*/
	string query;			/*user can paste gene sequence directly*/
	string gene_id; 		/*gene_id is a KBase feature id*/


    	list<genome_id> genome_ids; 	/*database to search against*/
    	string blast_program;		/*BLAST input parameters, blastp, blastn or etc.*/
    	float e-value;			/*BLAST input parameters*/
	#float coverage;			/*BLAST input parameters, alignment coverage*/
	float identity;			/*BLAST input parameters, sequence identity*/
	float score;			/*BLAST input parameters, blast summary score*/

    } BlastGenomeParams;

    typedef structure {
    	string gene_id;			/*gene_id is a KBase feature id*/
    	float e-value;			/*BLAST input parameters*/
	#float coverage;			/*BLAST input parameters*/
	float identity;			/*BLAST input parameters*/
	float score;			/*BLAST input parameters*/
    
    } hit;
    typedef list<hit> hits;



    /* description of method and parameters */
    funcdef blast_against_genome(BlastGenomeParams params) 
      			returns (blast_output_ref) authentication required;

};
