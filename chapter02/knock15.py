import sys 

file_name = sys.argv[1]
n = int(sys.argv[2])

with open(file_name,"r") as file:
    line_list = file.readlines()
    for line in line_list[-n:]:
        print(line.strip())

# tail -3 hightemp.txt


# ---- memo -----
# readlines()で一気に読み込むと
# 大規模なデータの場合にメモリを喰うので
# 一行ずつ読み込む方がいい
# キューとスタックで一行ずつ読み込める
