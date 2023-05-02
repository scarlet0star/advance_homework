def pascal(n):
    if n == 0:
        return [1]
    else:
        prev_row = pascal(n - 1)
        new_row = [1]
        
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        
        new_row.append(1)
        return new_row
print(pascal(5))

#prev_row = pascal(n-1)을 생각하기 힘들었다. 그런데 for루프로만 구성하면 더 편하지 않나...?