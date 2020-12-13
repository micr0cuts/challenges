import hashlib

inp = 'ckczppom'
toy = 'pqrstuv'

for i in range(10000000):
    m = hashlib.md5()
    s = inp + str(i)
    m.update(s.encode())

    if m.hexdigest().startswith('00000'):
        print("Solution to part1:", i)
        break

for i in range(10000000):
    m = hashlib.md5()
    s = inp + str(i)
    m.update(s.encode())

    if m.hexdigest().startswith('000000'):
        print("Solution to part2:", i)
        break