#!/bin/env python3

from subprocess import run, PIPE

count = 10

test_file = '/tmp/test.cpp'
a_out = '/tmp/a.out'

compilers = {
    'g++7':        ['g++-7', '-O3', test_file, '-o', a_out],
    'g++7/lto':    ['g++-7', '-O3', '-flto', test_file, '-o', a_out],
    'g++8':        ['g++', '-O3', test_file, '-o', a_out],
    'g++8/lto':    ['g++', '-O3', '-flto', test_file, '-o', a_out],
    'clang++':     ['clang++', '-O3', test_file, '-o', a_out],
    'clang++/lto': ['clang++', '-O3', '-flto', test_file, '-o', a_out],
}

code_base = """
#include <vector>

struct S {
    int i;
};
int main()
{
    std::vector<S> vec;
"""

results = {}
for k, v in compilers.items():
    sizes = []
    for n in range(count):
        with open(test_file, 'w') as fd:
            fd.write(code_base)
            for i in range(n):
                fd.write('vec.emplace_back();')
            fd.write('}')

        run(v).check_returncode()
        r = run(['objdump', '-j.text', '-h', a_out], stdout=PIPE)
        sizes.append(int(r.stdout.decode().split('\n')[5].split()[2], 16))
    results[k] = sizes


s=''.join(k.ljust(10) for k in compilers.keys())
print(s)
print('-'*len(s))
for n in range(count):
    print(''.join(str(v[n]).ljust(10) for v in results.values()))

import matplotlib.pyplot as plt
x = range(count)
for k, y in results.items():
    plt.plot(x, y, label=k)
plt.legend()
plt.show()
