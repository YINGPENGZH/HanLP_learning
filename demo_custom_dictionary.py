from pyhanlp import *


def demo_custom_dictionary(text):
    print(HanLP.segment(text))
    CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
    CustomDictionary.add("攻城狮")
    CustomDictionary.insert("白富美")
    # CustomDictionary.add("攻城狮")
    CustomDictionary.remove("攻城狮")
    CustomDictionary.insert("章雨晨")
    print(HanLP.segment(text))

if __name__=="__main__":
    text = "攻城狮逆袭单身狗，迎娶白富美，走上人生巅峰"  # 怎么可能噗哈哈！
    demo_custom_dictionary(text)