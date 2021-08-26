if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scores = student_marks[query_name]

   
    sum = 0.00
    for i in range(len(query_scores)):
        sum = sum + student_marks[query_name][i]
       
    avg = (sum / len(query_scores))
    format_float = "{:.2f}".format(avg)
    print(format_float) 
   