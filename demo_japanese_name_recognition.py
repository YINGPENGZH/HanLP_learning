from pyhanlp import *

def demo_japanese_name_recognition(sentences):
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    Term = JClass("com.hankcs.hanlp.seg.common.Term")

    segment = HanLP.newSegment().enableJapaneseNameRecognize(True)
    for sentence in sentences:
        term_list = segment.seg(sentence)
        print(term_list)

if __name__=="__main__":
    sentences = [
          "北川景子参演了林诣彬导演的《速度与激情3》",
           "林志玲亮相网友:确定不是波多野结衣？",
            "龟山千广和近藤公园在龟山公园里喝酒赏花",
        ]
    demo_japanese_name_recognition(sentences)
