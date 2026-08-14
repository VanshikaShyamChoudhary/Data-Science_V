import numpy as np
rng=np.arange(15)
print(rng)
print(rng.reshape(3,5))
rng=rng.reshape(3,5)
print(rng) # changed range
print(rng.ravel())# arranged sequence-1Darray
print(rng.shape)