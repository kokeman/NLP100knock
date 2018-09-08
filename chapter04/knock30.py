import MeCab
import os

def get_morpheme_list():
    '''
    「吾輩は猫である」を形態素解析した結果の各単語を、
    表層形(surface)、基本形(base)、品詞(pos)、品詞分類１(pos1)
    をキーとする辞書に格納し、一文ずつでまとめてリストとして返す

    戻り値: 一文ごとの辞書を要素とするリスト
    '''
    neko_path = os.path.abspath('neko.txt.mecab')
    morpheme = {} 
    sentence = []
    result = []
    with open(neko_path,'r') as neko_file:
        for line in neko_file:
            line = line.rstrip() #stripだと先頭の空白文字が消える
            if line != 'EOS':
                # lineの列をそれぞれリストに格納
                columm = line.split('\t')[1].split(',')
                columm.insert(0,line.split('\t')[0])

                # 上の二行はこれでも書ける
                # line = ','.join(line.split(\t)).split(',')

                # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                morpheme = {'surface': columm[0], 'base': columm[7], 'pos': columm[1], 'pos1': columm[2]}

                sentence.append(morpheme)
                if columm[2] == '句点':
                    result.append(sentence[:]) #sentenceで渡すと次の行でappendしたものが消えてしまう
                    sentence.clear()
    return result

if __name__ == '__main__':
    result = get_morpheme_list()
    for sentence in result:
        print(sentence)

# mecab neko.txt -o neko.txt.mecab

