# Convert to YCbCr
import matplotlib.pyplot as plt


def showYCbCr(image):
    image = image.convert('YCbCr')
    # Plot
    plt.close()
    # Main Image
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title('[YCbCr]')
    # Y
    plt.subplot(2, 2, 2)
    plt.imshow(image.getchannel(0))
    plt.title('[Y]CbCr')
    # Cb
    plt.subplot(2, 2, 3)
    plt.imshow(image.getchannel(1))
    plt.title('Y[Cb]Cr')
    # Cr
    plt.subplot(2, 2, 4)
    plt.imshow(image.getchannel(2))
    plt.title('YCb[Cr]')
    # Show
    plt.show()
