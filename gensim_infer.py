from gensim.models import Word2Vec
model = Word2Vec.load("word2vec.model")

a = model.wv.most_similar("man")
print(a)