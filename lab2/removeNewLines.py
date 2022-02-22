import os

dir = ''
for file in os.listdir(dir):
    f = open(dir + '/' + file, 'r+')
    i = 0
    final = ""
    for line in f:
        if line.split(',')[0] == 'step':
            final += line
            continue
        if i % 2 == 0:
            stripped_line = line.rstrip()
            final += stripped_line
        else:
            final += line
        i += 1
    f.seek(0)
    f.write(final)
    f.truncate()
    f.close()