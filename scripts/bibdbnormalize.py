#!/usr/bin/env python3

from enum import IntEnum ; 

"""
A script that reads 
"""

# This information was collected from 
#     http://bib-it.sourceforge.net/help/fieldsAndEntryTypes.php

entry_types = ['article', 'book', 'booklet', 'inbook', 'incollection', 
    'inproceedings', 'manual', 'mastersthesis', 'misc', 'phdthesis', 
    'proceedings', 'techreport', 'unpublished' ] ;
knwn_field_names = ['address', 'annote', 'author', 'booktitle', 'chapter', 
    'crossref', 'edition', 'editor', 'howpublished', 'institution', 'journal',
    'key', 'month', 'note', 'number', 'organization', 'pages', 'publisher', 
    'school', 'series', 'title', 'type', 'volume', 'year' ] ;
unkwn_field_names = ['doi', 'abstract' ] ;
entries = [('article', 
              ['author', 'title', 'journal', 'year'],
              ['volume', 'number', 'pages', 'month', 'note']),
           ('book',
              ['author', 


PubType = IntEnum('PubType', entry_types) ;
Field   = IntEnum('FieldType', field_names) ; 



