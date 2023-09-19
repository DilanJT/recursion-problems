

def fibonaci_sequence_implementation(n):
    counter = 0
    fibonaci_list = []
    a, b = 0, 1
    current_num = 0
    fibonaci_list.append(current_num)
    counter += 1
    
    current_num += 1
    fibonaci_list.append(current_num)
    counter += 1
    while(counter <= n):
        current_num = fibonaci_list[a] + fibonaci_list[b]
        fibonaci_list.append(current_num)
        a, b = a + 1, b + 1
        counter += 1
    return fibonaci_list
    
    
print(fibonaci_sequence_implementation(8))