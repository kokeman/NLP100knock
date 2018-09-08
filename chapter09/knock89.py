'''
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ
'''
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sklearn.externals import joblib
from operator import itemgetter
from gensim.models import word2vec


# matrix_300 = joblib.load('matrix_300') 
# vocab = joblib.load('vocab')

# vec_Spain = matrix_300[vocab['Spain']].reshape(1, -1)
# vec_Madrid = matrix_300[vocab['Madrid']].reshape(1, -1)
# vec_Athens = matrix_300[vocab['Athens']].reshape(1, -1)

# vec = vec_Spain - vec_Madrid + vec_Athens

# cos_sim_list = []
# for i in range(len(vocab)):
#     cos_sim = cosine_similarity(vec, matrix_300[i].reshape(1, -1))
#     cos_sim_list.append(((i, cos_sim)))

# cos_sim_list.sort(key=itemgetter(1), reverse=True)

# for i, cos_sim in cos_sim_list[0:10]:
#     word = [k for k, v in vocab.items() if v == i]
#     print(f'{i}\t{word}\t{cos_sim}')

'''
672     ['Spain']       [[0.81015035]]
6002    ['Austria']     [[0.79771792]]
1743    ['Sweden']      [[0.78695112]]
827     ['Italy']       [[0.77846448]]
1450    ['Germany']     [[0.77022373]]
15191   ['Belgium']     [[0.74642298]]
2197    ['Netherlands'] [[0.73991113]]
1637    ['Denmark']     [[0.73141804]]
134665  ['Télévisions'] [[0.72821381]]
6542    ['Vichy']       [[0.70957902]]
'''

model = word2vec.Word2Vec.load('../chapter10/w2v')
vec_Spain = model.wv['Spain'].reshape(1, -1)
vec_Madrid = model.wv['Madrid'].reshape(1, -1)
vec_Athens = model.wv['Athens'].reshape(1, -1)

vec = vec_Spain - vec_Madrid + vec_Athens

results = model.wv.most_similar(positive=vec)
for result in results[:10]:
    print(result)

'''
('Spain', 0.9037083387374878)
('Italy', 0.8570425510406494)
('Sweden', 0.818597137928009)
('Denmark', 0.815753698348999)
('Austria', 0.8083899617195129)
('Egypt', 0.7911469340324402)
('Belgium', 0.7894356846809387)
('Greece', 0.7892603278160095)
('Portugal', 0.7872555255889893)
('Russia', 0.7857146859169006)
'''