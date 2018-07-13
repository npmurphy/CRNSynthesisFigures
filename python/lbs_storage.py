import re
import argparse
from glob import glob
import os.path
import pandas as pd


def strip_reaction(reaction):
    rx = re.sub(r"2(s\d)", r"\1 + \1", reaction)
    strip_s = re.sub(r"s(\d)", r"\1", rx)
    strip_r = re.sub(r" ->{r\d} ", "", strip_s)
    strip_p = strip_r.replace(" + ", "")
    return strip_p


def reactions_only(filepath):
    with open(filepath, "r") as rf:
        lns = [
            l.strip().replace(" |", "") for l in rf.readlines()
            if "->{r" in str(l)
        ]
    return lns


def get_sweeps(filepath):
    # sweep = { "name": str,
    #           "variables": tuple str,
    #           "assignments": list tuple str }
    #sre = r"directive\s+sweep\s+\(.*\)\s+=\s+{\s*(\(.*\))\s*=\s*[\(.*\)]}"
    with open(filepath, "r") as rf:
        sweeps = [ l.strip() for l in rf.readlines() if "directive sweep" in l]
        #sweeps = [ (l.strip()).match("directive sweep (.*) .*") for l in rf.readlines() if "directive sweep" in l]
        #from ast import literal_eval
        # sweep = sweeps[0]
        # name, variables, elements = sweep.split(" = ")
        # name = name.replace("directive sweep", "").strip()
        # variables = variables.replace("{", "").strip()
        # elements

    return sweeps

def compress_directory_of_crns(in_directory, parent, file_base):
        all_files = glob(os.path.join(in_directory, "*.lbs"))

        sweepoutname = os.path.join(parent, file_base + "_sweeps.txt")
        sweeps = get_sweeps(all_files[0]) 
        print(sweeps)
        
        with open(sweepoutname, "w") as sf:
            sf.writelines(sweeps)

        outname = os.path.join(parent, file_base +"_CRNs.tsv")
        with open(outname, "w") as fo:
            fo.write("\t".join(["crn", "r0", "r1", "r2"]) + "\n")

            for path in all_files:
                crn_file = os.path.basename(path)
                crnnum = int(re.match(r"Bimol_(\d+)\.lbs", crn_file).groups()[0])
                basic_info = [strip_reaction(l) for l in reactions_only(path)]
                fo.write("\t".join([str(crnnum)] + basic_info) + "\n")
        
        
def get_lbs_code(crn_storage_file, crn_reacts, Nr, Ns):
    sweeps_file = crn_storage_file = crn_storage_file.replace("CRNs.tsv", "sweeps.txt")
    with open(sweeps_file, "r") as sf:
        sweeps = "\n".join(sf.readlines())

    inits = " |\n".join([ "init s{0} i{0}".format(s) for s in range(Ns)])
    rates = [ " r{0}, (0.01,100.0), 1.0, real, random".format(r) for r in range(Nr)]
    spaceing = "\n                     ;"
    rate_parameters = spaceing.join(rates)
    params = [ " i{0} = 10.0".format(i) for i in range(Ns) ]
    prams_str = spaceing.join(params)
    parameters = rate_parameters + spaceing + prams_str 
    
    file_code = """
directive simulation cmestiff
directive parameters [{3} ] 
{0}

directive fit_run {{ burnin      = 10
                  ; samples     = 10
                  ; mle_burnin  = 5
                  ; mle_samples = 5
                  ; thin        = 1 }}

{1}|
{2}
    """

    return file_code.format(sweeps, crn_reacts, inits, parameters)
        
        
def recover_crn(directory, crn_storage_file, regen, fmt="lbs"):

    #crn_storage_file = "/tmp/AMno11_S3_R3_CRNs.tsv"
    ns, nr = re.match(r".*_S(\d+)_R(\d+)_.*\.tsv", crn_storage_file).groups()
    Ns = int(ns)
    Nr = int(nr)
    crn_s = pd.read_csv(crn_storage_file, sep="\t", index_col="crn", dtype=str)

    def num_to_reaction(r, cr): return "s{0} + s{1} ->{{{4}}} s{2} + s{3}".format(*cr,r)

    def regenerate(crn_num):
        crn = crn_s.loc[crn_num].to_dict()
        crn_str = "|\n".join([ num_to_reaction(r, cr) for r, cr in crn.items() ])

        try:
            os.mkdir(directory)
        except FileExistsError as e:
            pass
        
        out_file_path = os.path.join(directory, "Bimol_{0}.{1}".format(crn_num, fmt)) 
        
        gened_code = ""
        if fmt == "crn":
            gened_code = ""
        elif fmt == "lbs":
            gened_code = get_lbs_code(crn_storage_file, crn_str, Nr, Ns)
        
        with open(out_file_path, "w") as co:
            co.write(gened_code)

    if regen == "all": 
        for idx,row in crn_s.iterrows(): 
            regenerate(idx)
    else: regenerate(int(regen))



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", '--directory', type=str)
    parser.add_argument("-c", '--compress', action="store_true", default=False)
    ## Extract flags
    parser.add_argument('--crn_storage_file', type=str)
    parser.add_argument("-r", '--regenerate', type=str)
    pa = parser.parse_args()
	
    print(pa.regenerate)

    fpar = pa.directory
    if pa.directory[-1] == os.path.sep:
        fpar = pa.directory[:-1]
    parent = os.path.dirname(fpar)
    file_base = os.path.basename(fpar)

    if pa.compress:
        compress_directory_of_crns(pa.directory, parent, file_base)

    if pa.regenerate:
	    recover_crn(pa.directory, pa.crn_storage_file, pa.regenerate)



if __name__ == "__main__":
    main()