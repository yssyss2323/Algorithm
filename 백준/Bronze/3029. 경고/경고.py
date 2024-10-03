curr_time = list(map(int, input().split(':')))
that_time = list(map(int, input().split(':')))

curr_tot = 3600 * curr_time[0] + 60 * curr_time[1] + curr_time[2]
that_tot = 3600 * that_time[0] + 60 * that_time[1] + that_time[2]
if that_tot <= curr_tot:
    that_tot += 24 * 3600

tmp = that_tot - curr_tot
h, tmp = divmod(tmp, 3600)
m, s = divmod(tmp, 60)

def tf(num):
    st = str(num)
    if len(st) < 2:
        st = '0' + st
    return st

print(f"{tf(h)}:{tf(m)}:{tf(s)}")