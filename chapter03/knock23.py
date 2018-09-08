import re

# == Level == 2~5まで
pattern = re.compile(r'^(={2,5})(.+)(\1)$')

with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    for line in read_file:
        match = pattern.search(line)
        if match:
            s = match.group(0)
            level = int(sum(c == '=' for c in s)/2 - 1)
            print(match.group(2).strip(), level)


# \数字で前に出たグループを指定できる
# {m,n}でm回以上n回以下の繰り返し
