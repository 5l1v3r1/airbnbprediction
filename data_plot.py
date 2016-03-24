from data_parse import Parser

import numpy as np

parser_train 	= Parser("session/train_data_sessions_pop.csv")

attributes 	= [
	'action_count', 'age', 'secs_elapsed'
]

data_instances 	= parser_train.get_data(attributes)
for instance in data_instances:
	if instance[0] > 100:
		print instance

classification 	= parser_train.get_class("booked")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA


X = np.array(data_instances[:100])
Y = np.array(classification[:100])


x_min, x_max = X[:, 0].min()-5, X[:, 0].max()+5
y_min, y_max = X[:, 1].min()-5, X[:, 1].max()+5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('action_count')
plt.ylabel('age')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))

ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(np.array(data_instances[:100]))

ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y,
           cmap=plt.cm.Paired)

ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.set_ylabel("2nd eigenvector")
ax.set_zlabel("3rd eigenvector")

plt.show()