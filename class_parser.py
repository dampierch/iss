from csv import DictReader
from os import environ
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
    ## choose module to parse results
    ## first set of combinations
    if l == ['L', 'L', 'L']:
        inconclusive_mod(d)
    elif l == ['L', 'L', 'M']:
        suggestive_by_1_mod(d)
    elif l == ['L', 'L', 'H']:
        match_by_1_mod(d)
    elif l == ['L', 'M', 'L']:
        suggestive_by_1_mod(d)
    elif l == ['L', 'M', 'M']:
        suggestive_by_2_mod(d)
    elif l == ['L', 'M', 'H']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['L', 'H', 'L']:
        match_by_1_mod(d)
    elif l == ['L', 'H', 'M']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['L', 'H', 'H']:
        match_by_2_mod(d)
    ## second set of combinations
    elif l == ['M', 'L', 'L']:
        suggestive_by_1_mod(d)
    elif l == ['M', 'L', 'M']:
        suggestive_by_2_mod(d)
    elif l == ['M', 'L', 'H']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['M', 'M', 'L']:
        suggestive_by_2_mod(d)
    elif l == ['M', 'M', 'M']:
        suggestive_by_3_mod(d)
    elif l == ['M', 'M', 'H']:
        match_by_1_sug_by_2_mod(d)
    elif l == ['M', 'H', 'L']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['M', 'H', 'M']:
        match_by_1_sug_by_2_mod(d)
    elif l == ['M', 'H', 'H']:
        match_by_2_sug_by_1_mod(d)
    ## third set of combinations
    elif l == ['H', 'L', 'L']:
        match_by_1_mod(d)
    elif l == ['H', 'L', 'M']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['H', 'L', 'H']:
        match_by_2_mod(d)
    elif l == ['H', 'M', 'L']:
        match_by_1_sug_by_1_mod(d)
    elif l == ['H', 'M', 'M']:
        match_by_1_sug_by_2_mod(d)
    elif l == ['H', 'M', 'H']:
        match_by_2_sug_by_1_mod(d)
    elif l == ['H', 'H', 'L']:
        match_by_2_mod(d)
    elif l == ['H', 'H', 'M']:
        match_by_2_sug_by_1_mod(d)
    elif l == ['H', 'H', 'H']:
        match_by_3_mod(d)
    else:
        print('parsing problem')


def main():
    ## prepare the inputs
    data = load_data()
    std_res = make_standard_res_dict()
    fam_dict = make_families_dict()
    ## parse the inputs
    for k in data.keys():
        d = set_values(data[k], std_res, fam_dict)
        parse_classes(d)


if __name__ == '__main__':
    main()
else:
    print('functions loaded for', modname)