import numpy as np

def conv_transform(image):
    image_copy = image.copy()

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image_copy[i][j] = image[image.shape[0]-i-1][image.shape[1]-j-1]
    return image_copy

def conv(image, kernel):
    kernel = conv_transform(kernel)
    image_h = image.shape[0]
    image_w = image.shape[1]

    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]

    h = kernel_h//2
    w = kernel_w//2

    image_conv = np.zeros(image.shape)

    for i in range(h, image_h-h):
        for j in range(w, image_w-w):
            sum = 0

            for m in range(kernel_h):
                for n in range(kernel_w):
                    sum = sum + kernel[m][n]*image[i-h+m][j-w+n]
            image_conv[i][j] = sum
    return image_conv