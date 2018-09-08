from knock41 import get_chunk_list
from itertools import combinations
from itertools import product

def get_path_to_root(line, chunk):
    '''
    chunkから根までに通るChunkオブジェクトのリストを返す
    line: 一文のチャンクのリスト
    chunk: Chunkクラスのオブジェクト
    return Chunkオブジェクトのリスト(chunkを含まない)
    '''
    dst = chunk.dst
    path = []
    if dst == -1:
        return path
    while dst != -1:
        path.append(line[dst])
        dst = line[dst].dst
    return path

def path_to_text(path):
    '''Chunkオブジェクトを要素とするリストを受け取り
    　　 そのオブジェクトの表層形を
        '-> surface -> surface -> surface'
        の形にして返す
    '''
    result = ''
    for chunk in path:
        result += '-> ' + chunk.normalized_surface()
    return result

def get_path_to_cross(path,cross):
    '''pathからcrossまでのオブジェクトを要素とするリストを返す'''
    result = []
    for chunk in path:
        result.append(chunk)
        if chunk is cross:
            return result
        return result

with open('result49','w') as output_file:
    for line in get_chunk_list():
        # 名詞を含む文節の組み合わせを取得
        noun_chunk = []
        for chunk in line:
            if chunk.check_pos('名詞'):
                noun_chunk.append(chunk)
        pairs = list(combinations(noun_chunk,2))

        for pair in pairs:
            x, y = pair

            # output_file.write(f'{x.normalized_surface()} {y.normalized_surface()}\n')
            # print(f'{x.normalized_surface()} {y.normalized_surface()}')
            
            # # 根までのパスを取得
            x_path = get_path_to_root(line, x)
            y_path = get_path_to_root(line, y)

            # print('diff:' + '[' +  ','.join([x.normalized_surface() for x in diff]) + ']')
            # print('diff:' + '[' +  ','.join([y.normalized_surface() for y in diff]) + ']')

            # 根までの経路で共通する文節を取得
            diff = list(set(x_path) & set(y_path))
            # diff = []
            # for x, y in product(x_path, y_path):
            #     # print(x.surface(),y.surface())
            #     if x is y:
            #         diff.append(x)
            
            # output_file.write('diff:' + '[' +  ','.join([d.normalized_surface() for d in diff]) + ']' + '\n')
            
            # XとYの助詞があれば取得
            X_av = x.get_surfaces('pos','助詞')
            Y_av = y.get_surfaces('pos','助詞')
            if X_av:
                X_av = X_av[-1]
            else:
                X_av = ''
            if Y_av:
                Y_av = Y_av[-1]
            else:
                Y_av = ''

            # xから根までのパスにyが存在する
            if y in x_path:
                path = x_path[:x_path.index(y)]

                middle = path_to_text(path)
                if middle == '':
                    middle = '->'

                output_file.write(f'X{X_av} {middle} Y\n')

            elif x in y_path:
                path = y_path[:y_path.index(x)]

                middle = path_to_text(path)
                if middle == '':
                    middle =  '->'

                output_file.write(f'X{X_av} {middle} Y\n')

            # xとyが根に至る経路上の文節kで交わる場合
            elif len(diff) >= 1:
                # 交差する文節を取得
                cross = diff[0]

                # 交差する文節までのパスをそれぞれ取得
                x_path = x_path[:x_path.index(cross)]
                y_path = y_path[:y_path.index(cross)]

                # x_path = get_path_to_cross(x_path,cross)
                # y_path = get_path_to_cross(y_path,cross)
                
                # print(''.join([x.normalized_surface() for x in x_path]))
                # print(''.join([y.normalized_surface() for y in y_path]))
                # print('-------------------')
                
                x_path_txt = path_to_text(x_path)
                y_path_txt = path_to_text(y_path)
                cross_txt = cross.normalized_surface()

                output_file.write(f'X{X_av}{x_path_txt} | Y{Y_av}{y_path_txt} | {cross_txt} \n')

            # # get_path_to_root関数の確認用
            # output_file.write(f'{x.normalized_surface()}')
            # for path in x_path:
            #     output_file.write(f' -> {path.normalized_surface()}')
            # output_file.write('\n')
            
            # output_file.write(f'{y.normalized_surface()}')
            # for path in y_path:
            #     output_file.write(f' -> {path.normalized_surface()}')
            # output_file.write('\n\n')
