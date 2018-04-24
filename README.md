
# Data type explainations
## Summary files (`summary_*.tsv`)
The columns are as follows:
* `CRN`	the CRN number.
* `unique` is the CRN the exemplar for a specification isomorphic class.
* `one` the unoptimized score (rate 1.0).
* `score` the best optimized rate. 
* `r0` reaction 0 optimised rate.
* `r1` reaction 1 optimised rate etc.

## Heatmap files (`Bimol_*.tsv`)
The columns are as follows:
* Column 0 input `s0` initial value.
* Column 1 input `s1` initial value.
* Column 2 unoptimized score (rate 1.0).
* Column 3 optimized score.

## Hitting time files (`Bimol_*.time`)
The columns are as follows:
* `i1` initial values of species `s1` etc. 
* `r0` optimized rate for reaction `r0` etc. 
* `opt_time` absorption time of rates (r0, r1 etc)
* `one_time` absorption time with rates all 1.0.

## Time-accuracy trade off files (Bimol_*.speedtime)
The columns are as follows:
* `i0` initial values of species `s0`. same for `i1` etc. 
* `r0` the optimized rate of reaction 0, same for `r1` etc. 
* `opt_time` the absorption time with optimised rates. 
* `one_time` the absorption time with rate 1.0. 
* `score` the accuracy of with the optimized rates.


# Figure 2:
Figure showing all the pre and post optimisation scores for AM_{3,3} and AM_{4,4} CRNs. Also shows the top scoring AM_{4,4} CRNs and shows how they compare to the top two AM_{3,3} CRNs.
## Data:
* `AMno11_S3_R3/summary_archetype.tsv`
    3 reactions 3 species Approximate Majority results.  
* `AMno11_S4_R4/summary_archetype.tsv`
    4 reactions 4 species Approximate Majority results.  
* `AMno11_S4_R4/summary_unique_subnets.tsv`
    4 reactions 4 species Approximate Majority results (specification isomorphic only) extra columns marking presence of different sub-networks. 

## Code:
* `python paper/fig_am_overview/overview_am_horiz.py`

# Figure 3
Heat maps of selected AM_{3,3} and AM_{4,4} CRNs.

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
Uncomment the appropriate directory in lines 8 to 13.

* `matlab Matlab/create_heatmaps.m`


# Figure 4
Figure showing the phase space and sepaatrix for two AM_{3,3} CRNs.
* `matlab Matlab/run_separatrix.m`

# Figure 5
Figure showing how long it takes to find CRNs with different numbers of reactions and species.
## Data
This data format is as follows
* Column 0 is the CRN number
* Column 1 is $K + 1$ where the CRN was found
* Column 2 is the time in seconds (since process start) when the CRN was found.

The files used are 
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_3_3.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_4_4.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_4_3.tsv`
* `paper/AMno11_z3_timmings/ApproximateMajorityNo11_3_4.tsv`

## Code
* `matlab Matlab/z3_am_time.m`

# Figure 6
Showing how CME calculations scale with species numbers. 
## Data 
The data for this figure is stored in 
* `Matlab/CMECalcEfficiency/times1.mat`
## Code
`matlab Matlab/CMECalcEfficiency/cme_am_time.m`

# Figure 7
Maximum 4 species 3 reactions, pre and post optimisation histograms.
## Data
* `paper/maximum_out_S4_R3/summary_archetype.tsv`
## Code
* `python paper/fig_max_speed_ac/fig_max_histo.py`

# Figure 8
Maximum 4 species 3 reactions, Example speed/accuracy trade off figure.
## Data
* `paper/maximum_out_S4_R3/Bimol_1.speedtime` Speed-accuracy trade off data
* `paper/maximum_out_S4_R3/Bimol_1.lbs` the CRN file used
## Code
* `python paper/fig_max_speed_ac/fig_max_histo.py`

# Figure 9 
Figure showing all the Division CRNs and how they score. 

## Data
These are the results of optimising all the Division CRNs.
* `paper/DivNsel_S3_R3/summary.tsv`
* `paper/DivNsel_S6_R2/summary.tsv`
* `paper/DivNsel_S3_R5/summary.tsv`
* `paper/DivNsel_S3_R2/summary.tsv`
* `paper/DivNsel_S5_R4/summary.tsv`
* `paper/DivNsel_S4_R5/summary.tsv`
* `paper/DivNsel_S5_R3/summary.tsv`
* `paper/DivNsel_S4_R2/summary.tsv`
* `paper/DivNsel_S4_R3/summary.tsv`
* `paper/DivNsel_S5_R2/summary.tsv`
* `paper/DivNsel_S3_R4/summary.tsv`
* `paper/DivNsel_S6_R3/summary.tsv`
* `paper/DivNsel_S4_R4/summary.tsv`

## Code
* `python paper/fig_div/fig_div_sumary.py` 