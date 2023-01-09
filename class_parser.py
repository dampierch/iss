from csv import DictReader
from os import environ
from glob import glob

from parser_families import make_families_dict


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
    d['v11_scr'] = d['Class1.score']
    for i in fam_dict['dkfz_v11_fam']:
        if d['Class1'].startswith(i, 0, len(i)):
            d['v11_scr'] = d['MCF1.score']
            break
    ## set v12 values
    d['v12_res'] = std_res[d['CNSv12b6.subclass1'].split(' :')[0]]
    d['v12_scr'] = d['CNSv12b6.subclass1.score']
    for i in fam_dict['dkfz_v12_fam']:
        if d['CNSv12b6.subclass1'].startswith(i, 0, len(i)):
            d['v12_scr'] = d['CNSv12b6.family.score']
            break
    ## set nci values
    d['nci_res'] = std_res[d['Consistency_class']]
    d['nci_scr'] = d['Consistency_score']
    for i in fam_dict['nci_fam']:
        if d['Consistency_class'].startswith(i, 0, len(i)):
            d['nci_scr'] = d['Consistency_family_score']
            break
    return d


def parse_classes(d, t1=0.50, t2=0.85):
    ## set score combination
    l = []
    scrs = ['v11_scr', 'v12_scr', 'nci_scr']
    for i in scrs:
        if float(d[i]) >= 0.3:
            if float(d[i]) >= 0.85:
                l.append('H')
            else:
                l.append('M')
        else:
            l.append('L')
    return l
    ## choose module to parse results
    if l == ['L', 'L', 'L']:
        inc_mod(d)
    else if ...


'''
data = load_data()
std_res = make_standard_res_dict()
fam_dict = make_families_dict()

for k in data.keys():
    d = set_values(data[k], std_res, fam_dict)
    XXX = parse_classes(d)

'''
