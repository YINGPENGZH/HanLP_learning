from pyhanlp import *

def demo_dependency_parser():
    sentence = HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。")
    for word in sentence.iterator():
        print("%s --(%s)--> %s" %(word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    word_array = sentence.getWordArray()
    for word in word_array:
        print("%s --(%s)--> %s" % (word.LEMMA, word.DEPREL, word.HEAD.LEMMA))
    print()

    CoNLLWord = JClass("com.hankcs.hanlp.corpus.dependency.CoNll.CoNLLWord")
    head = word_array[12]
    while head.HEAD:
        head = head.HEAD
        if(head == CoNLLWord.ROOT):
            print(head.LEMMA)
        else:
            print("%s --(%s)--> %s" % (head.LEMMA, head.DEPREL))

if __name__=="__main__":
    demo_dependency_parser()