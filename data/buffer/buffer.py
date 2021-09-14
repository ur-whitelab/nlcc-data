import numpy as np

pka = 4.76  
salt_conc = 0.30  # in M 
acid_conc = 0.20  # in M 

ph = pka + np.log10(salt_conc/acid_conc)
print(ph)


# check 
if np.isclose(ph, cal_ph(pka,salt_conc,acid_conc)) == True:
    result = True
else:
    result = False


