## modules for parsing in silico sample methylation classifier results


modname = 'parser_modules'


def inconclusive_mod(d):
    print('inconclusive_mod')
    s1 = 'DNA methylation-based tumor classification is inconclusive.'
    s2 = 'Results from all three classifiers are non-contributory.'


def suggestive_by_1_mod(d):
    print('suggestive_by_1_mod')


def match_by_1_mod(d):
    print('match_by_1_mod')


def suggestive_by_2_mod(d):
    print('suggestive_by_2_mod')


def match_by_1_sug_by_1_mod(d):
    print('match_by_1_sug_by_1_mod')


def match_by_2_mod(d):
    print('match_by_2_mod')


def suggestive_by_3_mod(d):
    print('suggestive_by_3_mod')


def match_by_1_sug_by_2_mod(d):
    print('match_by_1_sug_by_2_mod')


def match_by_2_sug_by_1_mod(d):
    print('match_by_2_sug_by_1_mod')


def match_by_3_mod(d):
    print('match_by_3_mod')


if __name__ == '__main__':
    print('no main function for', modname)
else:
    print('functions loaded for', modname)