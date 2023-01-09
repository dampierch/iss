## script to keep track of which classes should be evaluated at family level


modname = 'parser_families'


dkfz_v11_fam = [
    'ATRT',
    'ENB',
    'GBM',
    'LGG, PA',
    'MB, G',
    'MB, S',
    'PIN T, PB',
    'PLEX'
]


dkfz_v12_fam = [
    'ARMS',
    'ATRT',
    'EPN_PF',
    'EPN_SPINE',
    'EPN_ST',
    'ERMS',
    'GBM',
    'HGG',
    'LGG_MYB',
    'MB',
    'MNG',
    'MPNST',
    'NB',
    'PA',
    'PB',
    'pedHGG',
    'PPTID',
    'PTPR',
    'RB',
    'RMS'
]


nci_fam = [
    'ATRT',
    'EPN_PF',
    'EPN_REL',
    'EPN_SPINE',
    'EPN_ST',
    'eRMS',
    'ERMS',
    'ETMR',
    'GBM',
    'GBM_ped',
    'HGG',
    'HGNET_NOS',
    'ICMT',
    'LGG_MYB',
    'MB',
    'MNG',
    'MPNST',
    'NB',
    'PA',
    'PB',
    'pedHGG',
    'PPTID',
    'PTPR',
    'RB',
    'RMS-M'
]


def make_families_dict():
    d = {
        'dkfz_v11_fam': dkfz_v11_fam,
        'dkfz_v12_fam': dkfz_v12_fam,
        'nci_fam': nci_fam
    }
    return d


if __name__ == '__main__':
    print('no main function for', modname)
else:
    print('functions loaded for', modname)