def print_n_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)

print_n_times(5, "안녕", "하세요")