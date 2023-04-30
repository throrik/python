#! /user/bin/python3

import aptsources.sourceslist as sl

sources = sl.SourcesList()

for source in sources.list:
    if source.comment.lower().find("disabled on upgrade") >= 0:
        print(source)