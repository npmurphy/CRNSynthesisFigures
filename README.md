
# Data type explainations
## Summary files (`summary_*.tsv`)
* CRN	the CRN number
* unique: is the CRN the examplar for a specification isomorphic class.
* one: the unoptimized score (rate 1.0)
* score: the best optimized rate 
r0 reaction 0 optimised rate
r1 reaction 1 optimised rate
etc.

## Heatmap files (`Bimol_*.tsv`)
* Column 0 input `s0` initial value
* Column 1 input `s1` initial value
* Column 2 unoptimized score (rate 1.0)
* Column 3 optimized score 

## Hitting time files (`Bimol_*.time`)
* `i1` intial values of species `s1` etc. 
* `r0` value of reaction `r0` etc. 
* `opt_time` absorbtion time of rates (r0, r1 etc)
* `one_time` absorbtion time with rates all 1.0.


# Figure 2:
## Data:
* `AMno11_S3_R3/summary_archetype.tsv`
    3 reactions 3 species Approximate Majority results.  
* `AMno11_S4_R4/summary_archetype.tsv`
    4 reactions 4 species Approximate Majority results.  
* `AMno11_S4_R4/summary_unique_subnets.tsv`
    4 reactions 4 species Approximate Majority results (specification isomorphic only) extra columns marking presence of different subnetworks. 

## Code:
`python paper/fig_am_overview/overview_am_horiz.py`

# Figure 3

## Data

* `paper/AMno11_S3_R3/Bimol_28.lbs` The LBS file with reactions.
* `paper/AMno11_S3_R3/Bimol_28.time` The hitting time data.
* `paper/AMno11_S3_R3/Bimol_28.tsv` The heat map.
* `paper/AMno11_S3_R3/Bimol_36.lbs`
* `paper/AMno11_S3_R3/Bimol_36.time`
* `paper/AMno11_S3_R3/Bimol_36.tsv`
* `paper/AMno11_S4_R4/Bimol_3750.lbs`
* `paper/AMno11_S4_R4/Bimol_3750.time`
* `paper/AMno11_S4_R4/Bimol_3750.tsv`
* `paper/AMno11_S4_R4/Bimol_4854.lbs`
* `paper/AMno11_S4_R4/Bimol_4854.time`
* `paper/AMno11_S4_R4/Bimol_4854.tsv`



## Code
Uncomment the appropriate directroy in lines 8 to 13.

`matlab Matlab/create_heatmaps.m`


# Figure 4
`matlab Matlab/run_separatrix.m`

# Figure 5
## Data
This data format is as follows
* First column is the CRN number
* Second column is $K + 1$ where the CRN was found
* Third column is the time in seconds it was found at.

The files used are 
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_3_3.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_4_4.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_4_3.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_3_4.tsv`

## Code
`matlab Matlab/z3_am_time.m`

# Figure 6
