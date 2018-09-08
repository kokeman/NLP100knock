'''
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
'''
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.externals import joblib
from gensim.models import word2vec


# vocab = joblib.load('vocab')
# matrix_300 = joblib.load('matrix_300') 

# vec_United_States = matrix_300[vocab['United_States']].reshape(1, -1)
# vec_US = matrix_300[vocab['U.S']].reshape(1, -1)

# cos_sim = cosine_similarity(vec_United_States, vec_US)

# print(cos_sim)

# [[0.82959789]]

model = word2vec.Word2Vec.load('../chapter10/w2v')
cos_sim = model.similarity('United_States', 'U.S')
print(cos_sim)

# [[0.8601123]]