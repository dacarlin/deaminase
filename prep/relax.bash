#!/bin/bash

#$ -cwd 
#$ -S /bin/bash
#$ -e logs
#$ -o logs
#$ -N relax 

export ROSETTA3_DB=/share/tmp-data-1/siegellab/Rosetta/main/database
export PATH=$PATH:/share/tmp-data-1/siegellab/Rosetta/main/source/bin

relax.linuxgccrelease -in:file:s deaminase_model.pdb -renumber_pdb 1 -per_chain_renumbering 1 -constrain_relax_to_start_coords 1 -out:suffix ${SGE_TASK_ID} -extra_res_fa LG1.params 
