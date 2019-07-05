from pyhanlp import *

def demo_notional_tokenizer():
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    NotionalTokenizer = JClass("com.hankcs.hanlp.tokenizer.NotionalTokenizer")

    text = "小区居民有的反对喂养流浪猫，而有的居民却赞成喂养这些小宝贝"

    print(NotionalTokenizer.segment(text))
    for sentence in NotionalTokenizer.seg2sentence(text):
        print(sentence)

if __name__=="__main__":
    demo_notional_tokenizer()