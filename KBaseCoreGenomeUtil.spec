
module KBaseCoreGenomeUtil {


	/* @id ws KBaseGenomes.Genome */
	typedef string genome_ref;

	/* @id ws KBaseCoreGenomeUtil.BlastOutput */
	typedef string blast_output_ref;

    /*
    	@metadata ws length(hits) as Number of Hits
    */
    

    list<hit> hits;
    typedef structure{
    	string gene_id; /*gene_id is a KBase feature id*/
	float e-value; /*BLAST output parameters*/
	decimal coverage; /*BLAST output parameters*/
	float score; /*BLAST output parameters*/
	decimal identity;  /*BLAST output parameters*/
    } hit;
	

    typedef structure {

    	string gene_id; /*A KBase feature ID can be used as input if it is stored in the narrative*/
	string sequence; /*A protein/DNA sequence can also be used as input, directly pasted by users*/
	/*We only need one from gene_id or sequence*/

    	list<genome_ref> genomes; /*genomes for creating a BLAST database*/
	float e-value; /*BLAST input parameters*/
	decimal coverage; /*BLAST input parameters*/
	float score; /*BLAST input parameters*/
	decimal identity; /*BLAST input parameters*/

	string blast_type; /the types of BLAST, such as blastp or blastn/

    } BlastGenomeParams;

    /* description of method and parameters */
    funcdef blast_against_genomes(BlastGenomeParams params) returns (blast_output_ref) authentication required;

};
