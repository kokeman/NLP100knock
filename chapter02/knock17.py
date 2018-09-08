import sys

file_name = sys.argv[1]
file_ = open(file_name,"r")

set_pre = set()
for line in file_:
    line = line.strip()
    line_list = line.split("\t")
    set_pre.add(line_list[0])

for n in set_pre:
    print(n)

file_.close()

# python knock17.py col1.txt | sort | uniq

# 予約後は変数名に使わない