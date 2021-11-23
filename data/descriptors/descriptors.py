s = ['CC=O', 'CC=C=C(C(=O)N)']
v = get_descriptors(s)
result = True if np.shape(v) == (2, 8) else False
