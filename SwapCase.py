def  split(word):
    return[char for char in word]
def swap_case(s):
    str = ""
    str1 = split(s)    
    for i in range(len(str1)):
        if(str1[i].islower()):
            str1[i] = str1[i].upper()
        else:
            str1[i] = str1[i].lower()
        str += str1[i]
    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)