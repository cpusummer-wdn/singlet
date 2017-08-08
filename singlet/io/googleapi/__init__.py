# vim: fdm=indent
'''
author:     Fabio Zanini
date:       02/08/17
content:    Support module for filenames related to the Google Sheet APIs.
'''
# Modules
import os
import yaml

from singlet.config import config


# Process config
for sheetname, sheet in config['io']['samplesheets'].items():
    if ('google_id' not in sheet) and ('url' in sheet):
        url = sheet['url']
        config['io']['samplesheets'][sheetname]['google_id'] = url.split('/')[-1]