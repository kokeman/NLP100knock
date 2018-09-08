'''
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，その類似度を出力せよ．
'''
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.externals import joblib
from operator import itemgetter
from gensim.models import word2vec


# vocab = joblib.load('vocab')
# matrix_300 = joblib.load('matrix_300') 

# vec_England = matrix_300[vocab['England']].reshape(1, -1)

# cos_sim_list = []
# for i in range(len(vocab)):
#     cos_sim = cosine_similarity(vec_England, matrix_300[i].reshape(1, -1))
#     cos_sim_list.append(((i, cos_sim)))

# cos_sim_list.sort(key=itemgetter(1), reverse=True)

# for i, cos_sim in cos_sim_list[1:11]:
#     word = [k for k, v in vocab.items() if v == i]
#     print(f'{i}\t{word}\t{cos_sim}')

'''
4614    ['Wales']       [[0.66700253]]
4517    ['Scotland']    [[0.64105853]]
6001    ['Australia']   [[0.56419165]]
269     ['France']      [[0.52384244]]
672     ['Spain']       [[0.51961006]]
827     ['Italy']       [[0.51503805]]
1450    ['Germany']     [[0.49926728]]
1388    ['Ireland']     [[0.48937982]]
2640    ['Japan']       [[0.47636959]]
2198    ['Britain']     [[0.47227628]]
'''

model = word2vec.Word2Vec.load('../chapter10/w2v')
results = model.wv.most_similar(positive=['England'])
for result in results[:10]:
    print(result)

'''
('Wales', 0.790898859500885)
('Scotland', 0.7758111953735352)
('Ireland', 0.6801556944847107)
('Britain', 0.6282397508621216)
('London', 0.608329176902771)
('Liverpool', 0.584159255027771)
('Sweden', 0.5700684189796448)
('Manchester', 0.5656585097312927)
('Italy', 0.5591151714324951)
('Hampshire', 0.5575004816055298)
'''