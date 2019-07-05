from pyhanlp import *

def demo_URL_recognition(text):
    Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    URLTokenizer = JClass("com.hankcs.hanlp.tokenizer.URLTokenizer")

    term_list = URLTokenizer.segment(text)
    print(term_list)
    for term in term_list:
        if term.nature == Nature.xu:
            print(term.word)

if __name__=="__main__":
    text = '''HanLP的项目地址是https://github.com/hankcs/HanLP，
         发布地址是https://github.com/hankcs/HanLP/releases，
         我有时候会在www.hankcs.com上面发布一些消息，
        我的微博是http://weibo.com/hankcs/，会同步推送hankcs.com的新闻。
         听说.中国域名开放申请了,但我并没有申请hankcs.中国,因为穷……
       '''

    demo_URL_recognition(text)