def shell_sort(a_list):
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_pos in range(sublist_count):
            gap_insertion_sort(a_list,start_pos,sublist_count)
            

        sublist_count = sublist_count // 2




def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        pos = i
    
        while pos >= gap and a_list[pos-gap] > current_value:
            a_list[pos] = a_list[pos - gap]
            pos = pos - gap
    
        a_list[pos] = current_value

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)
