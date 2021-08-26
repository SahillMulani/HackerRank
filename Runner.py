if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    List = []
    for x in arr:
        List.append(x)
        
    List.sort()
    List.reverse() 
    for i in range(len(List)):
        if(List[i] != List[i+1]):
            print(List[i+1])
            break


    