import xml.etree.ElementTree as ET
import re

tree = ET.parse('nlp.txt.xml')

path_parse = './document/sentences/sentence/parse'

pattern = re.compile(r'^\((.*?) (.*)\)$', re.DOTALL)


def parse_s_expression(s, np_list):
    match = pattern.match(s)
    tag = match.group(1)
    value = match.group(2)

    depth = 0
    chunk = ''
    words = []
    for c in value:
        if c == '(':
            chunk += c
            depth += 1
        elif c == ')':
            chunk += c
            depth -= 1
            if depth == 0:
                words.append(parse_s_expression(chunk, np_list))
                chunk = ''
        else:
            if not (depth == 0 and c == ' '):
                chunk += c

    if chunk != '':
        words.append(chunk)

    if tag == 'NP':
        np_list.append(' '.join(words))

    return ' '.join(words)

for parse in tree.iterfind(path_parse):
    np_list = []
    parse_s_expression(parse.text.rstrip(), np_list)
    print(*np_list, sep='\n')
