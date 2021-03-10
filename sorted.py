#!/usr/bin/env python3

import collections
Entry = collections.namedtuple("Entry", ("location", "content"))
def sortedOrder():

    header = []
    packets = None
    _list = []
    with open("README.md" ,'r') as fp :
        for cnt, line in enumerate(fp):
            if cnt >= 14 :
                packets = line.split("|")
                _list.append(Entry(packets[2],line))
            else:
                header.append(line)


    # for index, entry in enumerate(_list):
    #     if index > 20 :
    #         break
    #     print(entry.location)

    _list.sort(key = lambda e : e.location) # Tim Sort
    with open("test.md", "w") as fp:
        for head in header:
            fp.write(head)
        for LINE in _list:
            fp.write(LINE.content)
    return









# start sorting
sortedOrder()
