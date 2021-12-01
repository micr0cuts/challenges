def inputgetter_list(fname):
    lines = []
    with open(fname, encoding='utf8') as f:
        for line in f:
            lines.append(line.strip())
    return lines
