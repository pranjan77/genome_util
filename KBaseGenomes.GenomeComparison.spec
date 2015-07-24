/*
Reference to a Proteome Comparison object in the workspace
@id ws GenomeComparison.ProteomeComparison
*/
typedef string Protcomp_ref;

/*
Reference to a Pangenome object in the workspace
@id ws KBaseGenomes.Pangenome
*/
typedef string Pangenome_ref;

/*
Reference to a Genome object in the workspace
@id ws KBaseGenomes.Genome
*/
typedef string Genome_ref;

/*
GenomeComparisonGenome object: this object holds information about a genome in a genome comparison
*/
typedef structure {
  string id;
  Genome_ref genome_ref;
  mapping<string, tuple<int, int>> genome_similarity;
  string name;
  string taxonomy;
  int features;
  int families;
  int functions;
} GenomeComparisonGenome;

/*
KBase Feature ID
@id external
*/
typedef string Feature_id;

/*
GenomeComparisonFamily object: this object holds information about a protein family across a set of genomes
*/
typedef structure {
  int core;
  mapping<string, list<tuple<Feature_id, list<int>, float>>> genome_features;
  string id;
  string type;
  string protein_translation;
  int number_genomes;
  float fraction_genomes;
  float fraction_consistent_annotations;
  string most_consistent_role;
} GenomeComparisonFamily;

/*
KBase Reaction ID
@id external
*/
typedef string Reaction_id;

/*
GenomeComparisonFunction object: this object holds information about a genome in a function across all genomes
*/
typedef structure {
  int core;
  mapping<string, list<tuple<Feature_id, int, float>>> genome_features;
  string id;
  list<tuple<Reaction_id, string>> reactions;
  string subsystem;
  string primclass;
  string subclass;
  int number_genomes;
  float fraction_genomes;
  float fraction_consistent_families;
  string most_consistent_family;
} GenomeComparisonFunction;

/*
GenomeComparisonData object: this object holds information about a multigenome comparison

@optional protcomp_ref pangenome_ref
@metadata ws core_functions as Core functions
    @metadata ws core_families as Core families
    @metadata ws name as Name
    @metadata ws length(genomes) as Number genomes
*/
typedef structure {
  string id;
  string name;
  int core_functions;
  int core_families;
  Protcomp_ref protcomp_ref;
  Pangenome_ref pangenome_ref;
  list<GenomeComparisonGenome> genomes;
  list<GenomeComparisonFamily> families;
  list<GenomeComparisonFunction> functions;
} GenomeComparison;
