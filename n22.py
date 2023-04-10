times = dict()
deps = dict()


def end_time(process):
    if deps[process] == ['0']:
        return times[process]
    else:
        return times[process] + max(end_time(pr_dep) for pr_dep in deps[process])

def start_time(process):
    return end_time(process) - times[process]


'22 статград'
l = open(r"C:\Users\karton\Desktop\InfaEGE\202303statgrad_22.txt").read().splitlines()

for i in l:
    process, time, tmp = i.split()
    times[process] = int(time)
    deps[process] = tmp.split(';')

# print(times, deps)
count = 0
for p in times.keys():
    print(p, #deps[p], times[p],
          start_time(p), end_time(p))
    if start_time(p) <= 150 <= end_time(p):
        count+=1

print(count)