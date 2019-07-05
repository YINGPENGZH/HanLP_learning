from pyhanlp import *
import time

def demo_basic_tokenizer(text):
    BasicTokenizer = JClass("com.hankcs.hanlp.tokenizer.BasicTokenizer")
    print(BasicTokenizer.segment(text))

    start = time.time()
    pressure = 100000
    for i in range(pressure):
        BasicTokenizer.segment(text)
    cost_time = time.time()-start
    print("BasicTokenizer分词速度：%.2f字每秒" % (len(text) * pressure / cost_time))

if __name__=="__main__":
    text = ("举办纪念活动铭记二战历史，不忘战争带给人类的深重灾难，是为了防止悲剧重演，确保和平永驻；"
    "铭记二战历史，更是为了提醒国际社会，需要共同捍卫二战胜利成果和国际公平正义，"
    "必须警惕和抵制在历史认知和维护战后国际秩序问题上的倒行逆施。")

    demo_basic_tokenizer(text)