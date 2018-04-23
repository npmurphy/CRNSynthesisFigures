
Summary files columsn
    CRN	the CRN number
    unique: is the CRN the examplar for a specification isomorphic class.
    one: the unoptimized score (rate 1.0)
    score: the best optimized rate 
    r0 reaction 0 optimised rate
    r1 reaction 1 optimised rate
    etc.

Figure 2:
Data:
    `AMno11_S3_R3/summary_archetype.tsv`
        3 reactions 3 species Approximate Majority results.  
    `AMno11_S4_R4/summary_archetype.tsv`
        4 reactions 4 species Approximate Majority results.  
    `AMno11_S4_R4/summary_unique_subnets.tsv`
        4 reactions 4 species Approximate Majority results (specification isomorphic only) extra columns marking presence of different subnetworks. 

Code:
    `python paper/fig_am_overview/overview_am_horiz.py`