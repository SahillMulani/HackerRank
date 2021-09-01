if __name__ == '__main__':
    List = []
    List1 = []
    n = int(input())
    for i in range(n):
        name = input()
        score = float(input())
        List.append([])
        List[i].extend([name,score])

    def takeSecond(elem):
        return elem[1]

    List.sort(key=takeSecond)

    
    print(List)
    j = 1 
    k = 0.0
    for i in range(n):
        if(List[i][j] != List[i+1][j]):
            k = List[i+1][j]
            break
    i = 0 
    for i in range(n):
        if( k == List[i][j]):
           List1.append(List[i][0])


    List1.sort()
    for i in range(len(List1)):
        print(List1[i])

 