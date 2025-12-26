def binary_search_with_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        value = arr[mid]

        if value == target:
            return iterations, value
        elif value < target:
            left = mid + 1
        else:
            upper_bound = value
            right = mid - 1
    return iterations, upper_bound

if __name__ == "__main__":
    data = [0.5, 1.2, 2.3, 3.8, 5.0, 7.4]

    print(binary_search_with_upper_bound(data, 3.8))
    print(binary_search_with_upper_bound(data, 4.0))
    print(binary_search_with_upper_bound(data, 0.1))
    print(binary_search_with_upper_bound(data, 10.0))

