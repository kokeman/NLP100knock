import re

# [[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]
pattern = re.compile(r'\[\[(?:ファイル|File):(?P<name>.+?)\|(.+)\]\]')

with open('Briten.txt','r', encoding = 'utf-8') as read_file:
    for line in read_file:
        match = pattern.search(line)
        if match:
            print(match.group('name'))

# (?P<name> )で名前をつけられる