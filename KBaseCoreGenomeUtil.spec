module KBaseCoreGenomeUtil {


	/* @id ws KBaseGenomes.Genome */
	typedef string genome_ref;

	/* @id ws KBaseCoreGenomeUtil.BlastOutput */
	typedef string blast_output_ref;

    /*
    	@metadata ws length(hits) as Number of Hits
    */
    typedef structure {
    	list<string> hits;
    } BlastOutput;


    typedef structure {

    	list<genome_ref> genomes;

    	string query;

    	string blast_program;
    	float e_value_cutoff;
    } BlastGenomeParams;

    /* description of method and parameters */
    funcdef blast_against_genome(BlastGenomeParams params) 
      			returns (blast_output_ref) authentication required;

};
