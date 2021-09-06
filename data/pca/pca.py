# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from matplotlib.pyplot import cm 

# load data
dist_data = np.loadtxt('pca-data.txt')
#print(dist_data.shape)


# do PCA 
pca = PCA(n_components = 2) 
pcs_data = pca.fit_transform(dist_data)
#print(pcs_data.shape)

pc1 = pcs_data[:,0]
pc2 = pcs_data[:,1]

"""
# plot
plt.figure()
plt.scatter(pc1, pc2, marker='x', c=np.arange(len(pc1))*1e-3,  cmap=plt.cm.get_cmap('viridis'))
cbar = plt.colorbar()
cbar.set_label('Time (ns)', fontsize=12)
plt.xlabel('PC1', fontsize=12)
plt.ylabel('PC2', fontsize=12)
plt.title("PC1 vs. PC2", fontsize=12)
plt.show()
"""

pc1_codex, pc2_codex = do_pca(dist_data,2)

# check
if np.all(np.abs(pc1 - pc1_codex) <= 1e-2) and np.all(np.abs(pc2 - pc2_codex) <= 1e-2) :
    result = True
else:
    result = False

