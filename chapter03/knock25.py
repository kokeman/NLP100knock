import re

# # {{基礎情報 国 ~ }}
# pattern_base_info = re.compile(r'''
#                                 ^\{\{基礎情報\s.+?$
#                                 (?P<base_info>.+?)
#                                 ^\}\}$
#                                 ''',re.MULTILINE | re.DOTALL | re.VERBOSE)

# |フィールド名 = 値
pattern_template = re.compile(r'''
                        ^
                        \|
                        (?P<field>.+?)
                        \s
                        =
                        \s
                        (?P<value>.+?)
                        (?=
                            \n
                            (\||\})
                        )
                        ''',re.MULTILINE | re.DOTALL | re.VERBOSE)

info_dict = {}
with open('Briten.txt','r',encoding = 'utf-8') as read_file:
    text = read_file.read()
    for match in pattern_template.finditer(text):
        info_dict[match.group('field')] = match.group('value')

for key, value in info_dict.items():
    print(key,value)

# X(?=Y) Xの後ろにYがあるXにマッチ
# MULTILINE 複数行マッチ
# DOTALL . が改行を含むすべての文字をマッチするようになる
# VERBOSE 空白が無視される

# info_dict = {}
# with open('Briten.txt','r',encoding = 'utf-8') as read_file:
#     text = read_file.read()

#     # 基本情報部分の抽出
#     match = pattern_base_info.match(text)
#     if match:
#         base_info = match.group('base_info')

#     # フィールドとバリューを抽出
#     for match in pattern_template.finditer(base_info):
#         info_dict[match.group('field')] = match.group('value')

# for key, value in info_dict.items():
#     print(key,value)