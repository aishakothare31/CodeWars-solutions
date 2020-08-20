def binary_array_to_number(arr):
  # given an array of ones and zeros, convert to integer
    s=''.join(str(i) for i in arr)
    return int(s,2)