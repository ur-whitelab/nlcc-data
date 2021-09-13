import numpy as np

dog_breeds = ['German Shepherd', 'Husky',
              'Bulldog', 'Dobermann', 'Great Dane', 'Husky', 'Bulldog', 'German Shepherd', 'Great Dane', 'German Shepherd']

unique_list = sorted(list(set(dog_breeds)))
n = len(dog_breeds)
m = len(unique_list)
ohe_array = np.zeros((n, m))
j = 0
for i in range(n):
        ohe_array[j, unique_list.index(dog_breeds[i])] = 1.
        j += 1

result = True if np.isclose(ohe(dog_breeds), ohe_array) else False
