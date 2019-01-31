# vim: fdm=indent
'''
author:     Fabio Zanini
date:       30/01/19
content:    Test parsing LOOM files.
'''
def test_loom_dataset():
    print('Parse integrated dataset as loom file')
    from singlet.io.loom import parse_dataset
    ds = parse_dataset(
        'example_data/dataset_PBMC.loom',
        axis_samples='columns',
        index_samples='_index',
        index_features='EnsemblID',
        )
    print('Done')