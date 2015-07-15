module KBaseCoreGenomeUtil {


	/* @id ws KBaseGenomes.Genome */
	typedef string genome_ref;

	/* @id ws KBaseCoreGenomeUtil.BlastOutput */
	typedef string blast_output_ref;

	/* reference of compare_genome_groups output object */
	typedef string compare_genome_groups_output_ref;





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



	/* Input parameters for compare_genome_groups function.

	   compare_genome_id -  ID of the compare_genome object used as input.
	   compare_genome_ws -  workspace ID the compare_genome object used as input.
	   genomes -  list of genomes in the pan genome from which compare_genome object is dervied
	   genome_workspaces - list of workspaces for genomes in the pan genome.
	   groups - list of groups for genomes in the pan genome object. 
	   output_id -  ID of the output object.

	 */



	typedef structure {
		string compare_genome_id;
		string compare_genome_ws;
		list<string> genomes;
		list<string> genome_workspaces;
		list <string> groups;
		string output_id;
	} compare_genome_groups_params;

	/* This function is used after running build_pangenome and compare_genomes functions. It takes 
	   a compare_genomes output (derived from pangenome object) as input. It also takes the broad groupings eg. rhizosphere, bulk-soil
	   for each genome. The output object is optimized for displaying comparison of groups.
	 */
	authentication required;
	funcdef compare_genome_groups(compare_genome_groups_params input) 
		returns (compare_genome_groups_output_ref);

};
