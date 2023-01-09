from csv import DictReader
from os import environ, mkdir
from glob import glob


from parser_families import make_families_dict
from parser_modules import inconclusive_mod, suggestive_by_1_mod, match_by_1_mod, suggestive_by_2_mod, match_by_1_sug_by_1_mod, match_by_2_mod, suggestive_by_3_mod, match_by_1_sug_by_2_mod, match_by_2_sug_by_1_mod, match_by_3_mod


modname = 'class_parser'


def load_data():
    ## read dkfz results
    f = glob(''.join([environ['TMP'], '*_KNN.combined.csv']))[0]
    d = {}
    with open(f, newline='') as csvfile:
	    reader = DictReader(csvfile)
	    for e in reader:
	        d[e['Sample']] = e
    ## read nci results
    f = ''.join([environ['TMP'], 'bin_classifier_output.csv'])
    d2 ={}
    with open(f, newline='') as csvfile:
	    reader = DictReader(csvfile)
	    for e in reader:
	        d2[e['Sample_name']] = e
    ## add nci results to dkfz results
    nci_fields = [
        'Consistency_class', 'Consistency_score', 'Consistency_family',
        'Consistency_family_score'
    ]
    for k in d.keys():
        for k2 in nci_fields:
            d[k][k2] = d2[k][k2]
    ## return data
    return d


def make_standard_res_dict():
    ## read subclass codes into standard result dict
    f = ''.join([environ['PWD'], '/', 'classifier_code_dict.tsv'])
    d ={}
    with open(f, newline='') as tsvfile:
	    reader = DictReader(tsvfile, delimiter='\t')
	    for e in reader:
	        d[e['subclass_code']] = e['standard_result']
    return d


def set_values(d, std_res, fam_dict):
    ## set v11 values
    d['v11_res'] = std_res[d['Class1']]
    d['v11_scr'] = '{:.3f}'.format(round(float(d['Class1.score']), 3))
    for i in fam_dict['dkfz_v11_fam']:
        if d['Class1'].startswith(i, 0, len(i)):
            d['v11_scr'] = '{:.3f}'.format(round(float(d['MCF1.score']), 3))
            break
    ## set v12 values
    d['v12_res'] = std_res[d['CNSv12b6.subclass1'].split(' :')[0]]
    d['v12_scr'] = '{:.3f}'.format(round(float(d['CNSv12b6.subclass1.score']), 3))
    for i in fam_dict['dkfz_v12_fam']:
        if d['CNSv12b6.subclass1'].startswith(i, 0, len(i)):
            d['v12_scr'] = '{:.3f}'.format(round(float(d['CNSv12b6.family.score']), 3))
            break
    ## set nci values
    d['nci_res'] = std_res[d['Consistency_class']]
    d['nci_scr'] = '{:.3f}'.format(round(float(d['Consistency_score']), 3))
    for i in fam_dict['nci_fam']:
        if d['Consistency_class'].startswith(i, 0, len(i)):
            d['nci_scr'] = '{:.3f}'.format(round(float(d['Consistency_family_score']), 3))
            break
    return d


def parse_classes(d, t1=0.50, t2=0.85):
    ## set score combination
    l = []
    scrs = ['v11_scr', 'v12_scr', 'nci_scr']
    for i in scrs:
        if float(d[i]) >= t1:
            if float(d[i]) >= t2:
                l.append('H')
            else:
                l.append('M')
        else:
            l.append('L')
    ## set results and scores dicts
    res = {'DKFZ v11': d['v11_res'], 'DKFZ v12': d['v12_res'], 'NCI': d['nci_res']}
    scr = {'DKFZ v11': d['v11_scr'], 'DKFZ v12': d['v12_scr'], 'NCI': d['nci_scr']}
    ## choose module to parse results
    ## first set of combinations
    if l == ['L', 'L', 'L']:
        cc, note = inconclusive_mod(d, res, scr)
    elif l == ['L', 'L', 'M']:
        cc, note = suggestive_by_1_mod(d, res, scr)
    elif l == ['L', 'L', 'H']:
        cc, note = match_by_1_mod(d, res, scr)
    elif l == ['L', 'M', 'L']:
        cc, note = suggestive_by_1_mod(d, res, scr)
    elif l == ['L', 'M', 'M']:
        cc, note = suggestive_by_2_mod(d, res, scr)
    elif l == ['L', 'M', 'H']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['L', 'H', 'L']:
        cc, note = match_by_1_mod(d, res, scr)
    elif l == ['L', 'H', 'M']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['L', 'H', 'H']:
        cc, note = match_by_2_mod(d, res, scr)
    ## second set of combinations
    elif l == ['M', 'L', 'L']:
        cc, note = suggestive_by_1_mod(d, res, scr)
    elif l == ['M', 'L', 'M']:
        cc, note = suggestive_by_2_mod(d, res, scr)
    elif l == ['M', 'L', 'H']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['M', 'M', 'L']:
        cc, note = suggestive_by_2_mod(d, res, scr)
    elif l == ['M', 'M', 'M']:
        cc, note = suggestive_by_3_mod(d, res, scr)
    elif l == ['M', 'M', 'H']:
        cc, note = match_by_1_sug_by_2_mod(d, res, scr)
    elif l == ['M', 'H', 'L']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['M', 'H', 'M']:
        cc, note = match_by_1_sug_by_2_mod(d, res, scr)
    elif l == ['M', 'H', 'H']:
        cc, note = match_by_2_sug_by_1_mod(d, res, scr)
    ## third set of combinations
    elif l == ['H', 'L', 'L']:
        cc, note = match_by_1_mod(d, res, scr)
    elif l == ['H', 'L', 'M']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['H', 'L', 'H']:
        cc, note = match_by_2_mod(d, res, scr)
    elif l == ['H', 'M', 'L']:
        cc, note = match_by_1_sug_by_1_mod(d, res, scr)
    elif l == ['H', 'M', 'M']:
        cc, note = match_by_1_sug_by_2_mod(d, res, scr)
    elif l == ['H', 'M', 'H']:
        cc, note = match_by_2_sug_by_1_mod(d, res, scr)
    elif l == ['H', 'H', 'L']:
        cc, note = match_by_2_mod(d, res, scr)
    elif l == ['H', 'H', 'M']:
        cc, note = match_by_2_sug_by_1_mod(d, res, scr)
    elif l == ['H', 'H', 'H']:
        cc, note = match_by_3_mod(d, res, scr)
    else:
        print('parsing problem')
    return cc, note


def write_values(k, d):
    ## make sub-dir within tmp to store values for each sample
    pn = ''.join([environ['TMP'], k, '/'])
    mkdir(pn)
    ## write all values to sub-dir
    fn = ''.join([pn, 'sample.tex'])
    with open(fn, 'w') as outfile:
        outfile.write(d['Sample'])
    ##
    fn = ''.join([pn, 'id.tex'])
    with open(fn, 'w') as outfile:
        outfile.write(d['ID'].replace('_', '\\_'))
    ##
    l = ['v11_res', 'v12_res', 'nci_res', 'v11_scr', 'v12_scr', 'nci_scr']
    for i in l:
        fn = ''.join([pn, i, '.tex'])
        with open(fn, 'w') as outfile:
            outfile.write(d[i])


def write_classes(k, cc, note):
    ## write classes to previously created sub-dir for sample
    pn = ''.join([environ['TMP'], k, '/'])
    ##
    fn = ''.join([pn, 'cc.tex'])
    with open(fn, 'w') as outfile:
        outfile.write(cc)
    ##
    fn = ''.join([pn, 'parsed_classes.tex'])
    with open(fn, 'w') as outfile:
        outfile.write(note)


def main():
    ## prepare the inputs
    data = load_data()
    std_res = make_standard_res_dict()
    fam_dict = make_families_dict()
    ## parse the inputs
    for k in data.keys():
        d = set_values(data[k], std_res, fam_dict)
        cc, note = parse_classes(d)
        write_values(k, d)
        write_classes(k, cc, note)


if __name__ == '__main__':
    main()
else:
    print('functions loaded for', modname)