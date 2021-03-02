import re

def getcache(cachetext):
    seppat = re.compile(r'[,+!@]')

    headers = None
    outlist = list()
    for line in cachetext:
        if line.startswith('Module'):
            headers = seppat.split(line)
#             print(headers)
            continue
        values = seppat.split(line)
        if len(values) == 7 and values[1].startswith('CACHE'):
            if not headers or len(headers) != len(values):
                raise RuntimeError('ERROR: could not find headers')
            valdict = dict()
            for i,k in enumerate(headers):
                valdict[k] = values[i] 
            # Above three lines quicker with: valdict = dict(zip(headers, values))
            outlist.append(valdict)
#             print(valdict)
    return outlist

getcache(cache)