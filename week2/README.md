W2

Basic NN:
Perceptron
AND Operator
OR Operator

--------

MiniFlow:
topological sort
python multiple length params *
zip operator 
np.dot vs np.multiply in Z = XW + b
np.reshape and np.concatenate -> flattening martices
	# 2 by 2 matrices
	w1  = np.array([[1, 2], [3, 4]])
	w2  = np.array([[5, 6], [7, 8]])

	# flatten
	w1_flat = np.reshape(w1, -1)
	w2_flat = np.reshape(w2, -1)

	w = np.concatenate((w1_flat, w2_flat))
	# array([1, 2, 3, 4, 5, 6, 7, 8])

multiple absolute mininma, local minima
why gradient descent can't gurantee best solution?

partial derivatives https://www.khanacademy.org/math/multivariable-calculus/multivariable-derivatives/partial-derivatives/v/partial-derivatives-introduction

python section slices https://docs.python.org/2.3/whatsnew/section-slices.html


backprop gradient chain on graphs https://www.youtube.com/watch?v=i94OvYb6noo

backpropagation jacobian matrix (effect of every item in X to the Z)

weights initialization: zero mean, small variance, image normalization (color_channel - 128)/128

cross validation

setting up an aws gpu -> http://cs231n.github.io/aws-tutorial/

sklearn LabelBinarizer -> one hot encode labels
sklearn train_test_split -> split data 



