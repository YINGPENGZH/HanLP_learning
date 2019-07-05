from pyhanlp import *

def demo_normalization():

    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    Config = JClass("com.hankcs.hanlp.HanLP$Config")

    Config.Normalization = True
    CustomDictionary.insert("爱听4G", "nz 1000")
    print(HanLP.segment("爱听4g"))
    print(HanLP.segment("爱听4G"))
    print(HanLP.segment("爱听４G"))
    print(HanLP.segment("爱听４Ｇ"))
    print(HanLP.segment("愛聽４Ｇ"))

if __name__=="__main__":
    demo_normalization()