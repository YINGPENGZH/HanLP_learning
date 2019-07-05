from pyhanlp import *

def demo_at_first_sight():
    print("首次编译运行时，HanLP会自动构建词典缓存，请稍候……")
    # HanLP.Config.enableDebug()
    print(HanLP.segment(
        "你好，欢迎使用HanLP汉语处理包！接下来请从其他Demo中体验HanLP丰富的功能~"))

if __name__=="__main__":
    demo_at_first_sight()