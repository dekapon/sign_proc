image = io.imread('Train-Data\Train-Data\hall\input' + filename + '.png')

    # cropping
    top = 15
    right = 12
    bottom = 35
    left = 50
    image = crop(image, ((top, bottom), (left, right), (0, 0)), copy=False)

    plt.rcParams['image.cmap'] = 'gray'
    image = color.rgb2gray(image)

    # pre
    size = (3, 3)
    im_open = ndimage.grey_opening(image, size=size)
    im_median = ndimage.median_filter(im_open, size=5)

    # edge detect
    edge_median = ndimage.sobel(im_median, axis=0)  # x

    # perform inverse binary thresholding
    sigma = 10
    blur = filters.gaussian(image, sigma=sigma)
    t = 0.3
    mask = blur > t

    im_masked = np.zeros_like(image)
    im_masked[mask] = im_median[mask]
# segmentation
    level1 = 0.6
    level2 = 0.4
    level3 = 0.09
    gray_r = im_masked.reshape(im_masked.shape[0] * im_masked.shape[1])
    for i in range(gray_r.shape[0]):
        if gray_r[i] > level1:
            gray_r[i] = 3
        elif gray_r[i] > level2:
            gray_r[i] = 2
        elif gray_r[i] > level3:
            gray_r[i] = 1
        else:
            gray_r[i] = 0
    im_segmented = gray_r.reshape(im_masked.shape[0], im_masked.shape[1])
    plt.imshow(im_segmented, cmap='gray')
    plt.show()

    # find contours
    contours = np.asarray(measure.find_contours(im_segmented, level=level3))

    # plot contours
    fig, ax = plt.subplots()
    ax.imshow(im_segmented, cmap=plt.cm.gray)

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

    plt.show()