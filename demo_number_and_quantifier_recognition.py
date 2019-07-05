from pyhanlp import *

def demo_number_and_quantifier_recognition(sentences):
    StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")

    StandardTokenizer.SEGMENT.enableNumberQuantifierRecognize(True)
    for sentence in sentences:
        print(StandardTokenizer.segment(sentence))

if __name__=="__main__":
    sentences = [
         "十九元套餐包括什么",
         "九千九百九十九朵玫瑰",
        "壹佰块都不给我",
           "９０１２３４５６７８只蚂蚁",
           "牛奶三〇〇克*2",
         "ChinaJoy“扫黄”细则露胸超2厘米罚款",
      ]
    demo_number_and_quantifier_recognition(sentences)