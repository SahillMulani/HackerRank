
vowels = ['A','E','I','O','a','e','i','o','u']

def subString(s, n):
    # n = len(String)
    vowels_point = 0
    con_point = 0
    for i in range(n):
        if s[i] in vowels:
            for len in range(i+1,n+1):
                vowels_point += 1
        else:
             for len in range(i+1,n+1):
                con_point += 1
    if vowels_point == con_point :
        print("Draw")
    elif vowels_point < con_point:
        print("Stuart")
        print(con_point)
    elif vowels_point > con_point:
        print("Kevin") 
        print(vowels_point)

if __name__ == '__main__':
    s = "BANANA"
    AllStrings = []
    subString(s,len(s))
   

 
