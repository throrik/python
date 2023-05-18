#! /user/bin/python3

import aptsources.sourceslist as sl

sources = sl.SourcesList()

# iterate over each source and find flag with disabled on upgrade
for source in sources.list:
    if source.comment.lower().find("disabled on upgrade") >= 0:
        print(source)
