from pyhanlp import *
from jpype import *

def demo_index_segment():
    Term = JClass("com.hankcs.hanlp.seg.common.Term")
    IndexTokenizer = JClass("com.hankcs.hanlp.tokenizer.IndexTokenizer")

    term_list = IndexTokenizer.segment("主副食品")
    for term in term_list.iterator():
        print("{} [{}:{}]".format(term, term.offset, term.offset+len(term.word)))

    print("最细颗粒度切分：")
    IndexTokenizer.SEGMENT.enableIndexMode(JInt(1))
    term_list = IndexTokenizer.segment("主副食品")
    for term in term_list.iterator():
        print("{} [{}:{}]".format(term, term.offset, term.offset + len(term.word)))

if __name__=="__main__":
    demo_index_segment()