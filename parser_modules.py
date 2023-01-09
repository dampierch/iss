## modules for parsing in silico sample methylation classifier results


modname = 'parser_modules'


def inconclusive_mod(d, r, s):
    print('inconclusive_mod')
    s1 = 'DNA methylation-based tumor classification is inconclusive.'
    s2 = 'Results from all three classifiers are non-contributory.'
    print(''.join([s1, s2]))
    cc = 'See note.'
    note = ''.join([s1, s2])
    return cc, note


def suggestive_by_1_mod(d, r, s):
    ## identify highest score classifier and return standardized result
    print('suggestive_by_1_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    hX = r[h1]
    s1 = 'There is no consensus methylation class match, but '
    s2 = 'the result from {} is suggestive of {}. '.format(h1, hX)
    s3 = 'Results from the other classifiers are non-contributory.'
    print(''.join([s1, s2, s3]))
    cc = 'See note.'
    note = ''.join([s1, s2, s3])
    return cc, note


def match_by_1_mod(d, r, s):
    ## identify highest score classifier and return standardized result
    print('match_by_1_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    hX = r[h1]
    s1 = 'There is no consensus methylation class match, but '
    s2 = 'the result from {} is a high-confidence match to {}. '.format(h1, hX)
    s3 = 'Results from the other classifiers are non-contributory.'
    print(''.join([s1, s2, s3]))
    cc = 'See note.'
    note = ''.join([s1, s2, s3])
    return cc, note


def suggestive_by_2_mod(d, r, s):
    ## identify highest 2 scoring classifiers and test whether same
    print('suggestive_by_2_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    if h1X == h2X:
        s2 = 'results from {} and {} are suggestive of {}. '.format(h1, h2, h1X)
    else:
        s2 = 'the result from {} is suggestive of {} while the result from {} is suggestive of {}. '.format(h1, h1X, h2, h2X)
    s1 = 'There is no consensus methylation class match, but '
    s3 = 'The result from {} is non-contributory.'.format(h3)
    print(''.join([s1, s2, s3]))
    cc = 'See note.'
    note = ''.join([s1, s2, s3])
    return cc, note


def match_by_1_sug_by_1_mod(d, r, s):
    ## identify highest 2 scoring classifiers and test whether same
    print('match_by_1_sug_by_1_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    if h1X == h2X:
        s2 = 'the result from {} is a high-confidence match to {} with suggestive support from {}. '.format(h1, h1X, h2)
    else:
        s2 = 'the result from {} is a high-confidence match to {} while the result from {} is suggestive of {}. '.format(h1, h1X, h2, h2X)
    s1 = 'There is no consensus methylation class match, but '
    s3 = 'The result from {} is non-contributory.'.format(h3)
    print(''.join([s1, s2, s3]))
    cc = 'See note.'
    note = ''.join([s1, s2, s3])
    return cc, note


def match_by_2_mod(d, r, s):
    ## identify highest 2 scoring classifiers and test whether same
    print('match_by_2_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    if h1X == h2X:
        s2 = 'results from {} and {} are high-confidence matches to {}. '.format(h1, h2, h1X)
    else:
        s2 = 'the result from {} is a high-confidence match to {} while the result from {} is a high-confidence match to {}. '.format(h1, h1X, h2, h2X)
    s1 = 'There is no consensus methylation class match, but '
    s3 = 'The result from {} is non-contributory.'.format(h3)
    print(''.join([s1, s2, s3]))
    cc = 'See note.'
    note = ''.join([s1, s2, s3])
    return cc, note


def suggestive_by_3_mod(d, r, s):
    ## sort classifiers and test equality of results
    print('suggestive_by_3_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    h3X = r[h3]
    if h1X == h2X:
        if h1X == h3X:
            s2 = 'results from {}, {}, and {} are suggestive of {}.'.format(h1, h2, h3, h1X)
        else:
            s2a = 'results from {} and {} are suggestive of {} while '.format(h1, h2, h1X)
            s2b = 'the result from {} is suggestive of {}.'.format(h3, h3X)
            s2 = ''.join([s2a, s2b])
    elif h1X == h3X:
        s2a = 'results from {} and {} are suggestive of {} while '.format(h1, h3, h1X)
        s2b = 'the result from {} is suggestive of {}.'.format(h2, h2X)
        s2 = ''.join([s2a, s2b])
    elif h2X == h3X:
        s2a = 'results from {} and {} are suggestive of {} while '.format(h2, h3, h2X)
        s2b = 'the result from {} is suggestive of {}.'.format(h1, h1X)
        s2 = ''.join([s2a, s2b])
    else:
        s2a = 'the result from {} is suggestive of {}, '.format(h1, h1X)
        s2b = 'the result from {} is suggestive of {}, and '.format(h2, h2X)
        s2c = 'the result from {} is suggestive of {}.'.format(h3, h3X)
        s2 = ''.join([s2a, s2b, s2c])
    s1 = 'There is no consensus methylation class match, but '
    print(''.join([s1, s2]))
    cc = 'See note.'
    note = ''.join([s1, s2])
    return cc, note


def match_by_1_sug_by_2_mod(d, r, s):
    ## sort classifiers and test equality of results
    print('match_by_1_sug_by_2_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    h3X = r[h3]
    if h1X == h2X:
        if h1X == h3X:
            s2a = 'the result from {} is a high-confidence match to {} with '.format(h1, h1X)
            s2b = 'suggestive support from {} and {}.'.format(h2, h3)
            s2 = ''.join([s2a, s2b])
        else:
            s2a = 'the result from {} is a high-confidence match to {} with '.format(h1, h1X)
            s2b = 'suggestive support from {} while '.format(h2)
            s2c = 'the result from {} is suggestive of {}.'.format(h3, h3X)
            s2 = ''.join([s2a, s2b, s2c])
    elif h1X == h3X:
        s2a = 'the result from {} is a high-confidence match to {} with '.format(h1, h1X)
        s2b = 'suggestive support from {} while '.format(h3)
        s2c = 'the result from {} is suggestive of {}.'.format(h2, h2X)
        s2 = ''.join([s2a, s2b, s2c])
    elif h2X == h3X:
        s2a = 'the result from {} is a high-confidence match to {} while '.format(h1, h1X)
        s2b = 'results from {} and {} are suggestive of {}.'.format(h2, h3, h2X)
        s2 = ''.join([s2a, s2b])
    else:
        s2a = 'the result from {} is a high-confidence match to {} while '.format(h1, h1X)
        s2b = 'the result from {} is suggestive of {}, and '.format(h2, h2X)
        s2c = 'the result from {} is suggestive of {}.'.format(h3, h3X)
        s2 = ''.join([s2a, s2b, s2c])
    s1 = 'There is no consensus methylation class match, but '
    print(''.join([s1, s2]))
    cc = 'See note.'
    note = ''.join([s1, s2])
    return cc, note


def match_by_2_sug_by_1_mod(d, r, s):
    ## sort classifiers and test equality of results
    print('match_by_2_sug_by_1_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    h3X = r[h3]
    if h1X == h2X:
        if h1X == h3X:
            s2a = 'results from {} and {} are high-confidence matches to {} with '.format(h1, h2, h1X)
            s2b = 'suggestive support from {}.'.format(h3)
            s2 = ''.join([s2a, s2b])
        else:
            s2a = 'results from {} and {} are high-confidence matches to {} while '.format(h1, h2, h1X)
            s2b = 'the result from {} is suggestive of {}.'.format(h3, h3X)
            s2 = ''.join([s2a, s2b])
    elif h1X == h3X:
        s2a = 'the result from {} is a high-confidence match to {} with '.format(h1, h1X)
        s2b = 'suggestive support from {} while '.format(h3)
        s2c = 'the result from {} is a high-confidence match to {}.'.format(h2, h2X)
        s2 = ''.join([s2a, s2b, s2c])
    elif h2X == h3X:
        s2a = 'the result from {} is a high-confidence match to {} with '.format(h2, h2X)
        s2b = 'suggestive support from {} while '.format(h3)
        s2c = 'the result from {} is a high-confidence match to {}.'.format(h1, h1X)
        s2 = ''.join([s2a, s2b, s2c])
    else:
        s2a = 'the result from {} is a high-confidence match to {} while '.format(h1, h1X)
        s2b = 'the result from {} is a high-confidence match to {}, and '.format(h2, h2X)
        s2c = 'the result from {} is suggestive of {}.'.format(h3, h3X)
        s2 = ''.join([s2a, s2b, s2c])
    s1 = 'There is no consensus methylation class match, but '
    print(''.join([s1, s2]))
    cc = 'See note.'
    note = ''.join([s1, s2])
    return cc, note


def match_by_3_mod(d, r, s):
    ## sort classifiers and test equality of results
    print('match_by_3_mod')
    h1 = sorted(s.items(), key=lambda item: -float(item[1]))[0][0]
    h2 = sorted(s.items(), key=lambda item: -float(item[1]))[1][0]
    h3 = sorted(s.items(), key=lambda item: -float(item[1]))[2][0]
    h1X = r[h1]
    h2X = r[h2]
    h3X = r[h3]
    if h1X == h2X:
        if h1X == h3X:
            s1 = 'There is a consensus methylation class match to {}.'.format(h1X)
            s2 = 'Results from all classifiers are high-confidence matches to {}'.format(h1X)
            cc = h1X
        else:
            s1 = 'There is no consensus methylation class match, but '
            s2a = 'results from {} and {} are high-confidence matches to {} while '.format(h1, h2, h1X)
            s2b = 'the result from {} is a high-confidence match to {}.'.format(h3, h3X)
            s2 = ''.join([s2a, s2b])
            cc = 'See note.'
    elif h1X == h3X:
        s1 = 'There is no consensus methylation class match, but '
        s2a = 'results from {} and {} are high-confidence matches to {} while '.format(h1, h3, h1X)
        s2b = 'the result from {} is a high-confidence match to {}.'.format(h2, h2X)
        s2 = ''.join([s2a, s2b])
        cc = 'See note.'
    elif h2X == h3X:
        s1 = 'There is no consensus methylation class match, but '
        s2a = 'results from {} and {} are high-confidence matches to {} while '.format(h2, h3, h2X)
        s2b = 'the result from {} is a high-confidence match to {}.'.format(h1, h1X)
        s2 = ''.join([s2a, s2b])
        cc = 'See note.'
    else:
        s1 = 'There is no consensus methylation class match. '
        s2a = 'The result from {} is a high-confidence match to {}, '.format(h1, h1X)
        s2b = 'the result from {} is a high-confidence match to {}, and '.format(h2, h2X)
        s2c = 'the result from {} is a high-confidence match to {}.'.format(h3, h3X)
        s2 = ''.join([s2a, s2b, s2c])
        cc = 'See note.'
    print(''.join([s1, s2]))
    note = ''.join([s1, s2])
    return cc, note


if __name__ == '__main__':
    print('no main function for', modname)
else:
    print('functions loaded for', modname)