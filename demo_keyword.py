from pyhanlp import *

def demo_keyword(content):
    TextRankKeyword = JClass("com.hankcs.hanlp.summary.TextRankKeyword")
    keyword_list = HanLP.extractKeyword(content,5)
    print(keyword_list)


if __name__=="__main__":
    content = (
    "程序员(英文Programmer)是从事程序开发、维护的专业人员。"     
    "一般将程序员分为程序设计人员和程序编码人员，"  
    "但两者的界限并不非常清楚，特别是在中国。"  
    "软件从业人员分为初级程序员、高级程序员、系统"    
    "分析员和项目经理四大类。")
    demo_keyword(content)