# Week 3

L2 regulariazation
L2 Norm of cost function

Dropout -> https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf

## Convnets

- Weight sharing
- Statistical invariance
- translation invariance

- filter (kernel) : kernel size is odd in general: 1, 3, 5 ...
- feature map, activation map
- stride
- padding 
	- https://stackoverflow.com/questions/37674306/what-is-the-difference-between-same-and-valid-padding-in-tf-nn-max-pool-of-t 
	- https://github.com/vdumoulin/conv_arithmetic

	- Same padding: SAME = pad enough so the output has the same dimensions as the input tensor.
	- VALID padding: no-padding

- number of filters (k) : power of 2 in general, to make computations efficient

- CNN structure https://www.youtube.com/watch?v=V8JDMkARdfU&list=PLlJy-eBtNFt6EuMxFYRiNRS07MCWN5UIA&index=7

- pooling
	- **max-pooling** : Conceptually, the benefit of the max pooling operation is to reduce the size of the input, and allow the neural network to focus on only the most important elements. Max pooling does this by only retaining the maximum value for each filtered area, and removing the remaining values. Tensorflow `tf.nn.max_pool()` function. (https://www.quora.com/What-is-max-pooling-in-convolutional-neural-networks)

	But, `Dropout` is a much better regularizer.

	Max pooling is done by applying a max filter to non-overlapping sub-regions of the initial representation.

	- average pooling

- 1x1 convolutions

- inception modules