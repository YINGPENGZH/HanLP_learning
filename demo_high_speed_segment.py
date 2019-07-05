from pyhanlp import *
import time
def demo_high_speed_segment():
    SpeedTokenizer = JClass("com.hankcs.hanlp.tokenizer.SpeedTokenizer")
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    JClass("com.hankcs.hanlp.HanLP$Config").ShowTermNature = False
    print(SpeedTokenizer.segment(text))

    start = time.time()
    pressure = 1000000
    for i in range(pressure):
        SpeedTokenizer.segment(text)
    cost_time = time.time()-start
    print("SpeedTokenizer分词速度：%.2f字每秒" % (len(text)*pressure/cost_time))

if __name__=="__main__":
    demo_high_speed_segment()

