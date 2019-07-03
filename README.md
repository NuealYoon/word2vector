임베딩 벡터를 훈력하는 라이브러리(Gensim, FastText)들을 사용하여 학습해 보고 있습니다.

현재 Gensim쪽만 보고 있습니다.

참고 하실 코드는 gensim_infer.py과 gensim_train.py 입니다.
gensim_train.py을 실행 시키면, .xml데이터를 학습하여 word2vector.model을 출력 시킵니다.

gensim_infer.py은 학습된 word2vector.model를 사용하여 'man'에 유사한 단어를 출력합니다.
