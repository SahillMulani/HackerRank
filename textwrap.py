import textwrap


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = textwrap.wrap(string, max_width)
    print(result)