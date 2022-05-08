def average(array):
    # your code goes here
    s = set()
    for i in array:
        s.add(i)
    sum = 0
    for i in s:
        sum = sum + i
    result = sum / len(s)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)