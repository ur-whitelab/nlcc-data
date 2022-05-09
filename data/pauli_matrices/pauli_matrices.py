
sx = np.array(((0,1),(1,0)))
sy = np.array(((0,-1j),(1j,0)))
sz = np.array(((1,0),(0,-1)))

sx_codex, sy_codex, sz_codex = pauli()
result = np.all(sx==sx_codex)*np.all(sy==sy_codex)*np.all(sz==sz_codex)

