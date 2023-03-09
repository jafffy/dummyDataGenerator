import numpy as np
import sys

num_instances = 8

if len(sys.argv) == 2:
    num_instances = int(sys.argv[1])

for i in range(num_instances):
    np.save(f'dummy_{2 ** i}MB.npy', np.random.random((512, 256, 2 ** i)))
