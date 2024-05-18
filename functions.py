def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """

    x_list = x.tolist()
    res = 1
    for i in range(0, min(len(x_list), len(x_list[0]))):
        if x_list[i][i] != 0:
            res *= x_list[i][i]
    return res


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """

    x_list = x.tolist()
    y_list = y.tolist()

    x_list.sort()
    y_list.sort()

    return x_list == y_list


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """

    x_list = x.tolist()
    n = len(x_list)
    mx = -1e9
    for i in range(1, n):
        if (x_list[i - 1] == 0 and x_list[i] > mx):
            mx = x_list[i]
    return mx


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """

    H, W, C = img.shape
    assert C == 3

    result = np.zeros((H, W))

    for i in range(H):
        for j in range(W):
            result[i, j] = img[i, j, 0] * coefs[0] + img[i, j, 1] * coefs[1] + img[i, j, 2] * coefs[2]

    return result




def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    x_list = x.tolist()
    
    if len(x_list) == 0:
        return [], []

    elements = []
    counters = []

    current_element = x_list[0]
    count = 1

    for i in range(1, len(x_list)):
        if x_list[i] == current_element:
            count += 1
        else:
            elements.append(current_element)
            counters.append(count)
            current_element = x_list[i]
            count = 1

    elements.append(current_element)
    counters.append(count)

    return elements, counters


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """

    x_list = x.tolist()
    y_list = y.tolist()
    distance_array = np.zeros((len(x_list), len(y_list)))

    for i in range(len(x_list)):
        for j in range(len(y_list)):
            distance_array[i, j] = np.sqrt(np.sum((x_list[i] - y_list[j]) ** 2))

    return distance_array
