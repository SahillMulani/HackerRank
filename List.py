if __name__ == '__main__':
    N = int(input())
    List = []

    for _ in range(N):
        i = input().split()
        command  = i[0]
        arguments = i[1:]
        if(command != 'print'):
            command += "("+",".join(arguments)+")"
            eval("List."+command)
        else:
            print(List)

