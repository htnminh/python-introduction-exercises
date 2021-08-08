def hanoi_tower(n):
    def transfer(n, start, end, mid):
        if n == 1:
            nonlocal count
            count += 1
            # print(start, '->', end)
        else:
            transfer(n - 1, start, mid, end)
            transfer(1, start, end, mid)
            transfer(n - 1, mid, end, start)
    count = 0
    transfer(n, 'start', 'end', 'mid')
    return count