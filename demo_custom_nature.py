from pyhanlp import *

def demo_custom_nature():
    Nature = JClass("com.hankcs.hanlp.corpus.tag.Nature")
    pc_nature = Nature.fromString("n")
    print(pc_nature)
    pc_nature = Nature.fromString("电脑品牌")
    print(pc_nature)
    pc_nature = Nature.create("电脑品牌")
    print(pc_nature)
    LexiconUtility = JClass("com.hankcs.hanlp.utility.LexiconUtility")
    LexiconUtility.setAttribute("苹果电脑",pc_nature)
    LexiconUtility.setAttribute("苹果电脑","电脑品牌 1000")
    term_list = HanLP.segment("苹果电脑可以运行开源阿尔法狗代码吗")
    print(term_list)
    for term in term_list:
        if term.nature == pc_nature:
            print("找到了 [{}] : {}\n".format(pc_nature, term.word))
    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    CustomDictionary.insert("阿尔法狗", "科技名词 1024")
    StandardTokenizer = JClass("com.hankcs.hanlp.tokenizer.StandardTokenizer")
    StandardTokenizer.SEGMENT.enablePartOfSpeechTagging(True)
    term_list = HanLP.segment("苹果电脑可以运行开源阿尔法狗代码吗")
    print(term_list)

if __name__=="__main__":
    demo_custom_nature()