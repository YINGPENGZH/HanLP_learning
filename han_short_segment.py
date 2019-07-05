from pyhanlp import *

def demo_NShort_segment(sentences):
    NShortSegment = JClass("com.hankcs.hanlp.seg.NShort.NShortSegment")
    Segment = JClass("com.hankcs.hanlp.seg.Segment")
    ViterbiSegment = JClass("com.hankcs.hanlp.seg.Viterbi.ViterbiSegment")

    nshort_segment = NShortSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True)
    shortest_segment = ViterbiSegment().enableCustomDictionary(False).enablePlaceRecognize(True).enableOrganizationRecognize(True)

    for sentence in sentences:
       print("N-最短分词：{}\n最短路分词：{}".format(nshort_segment.seg(sentence),shortest_segment.seg(sentence)))


if __name__=="__main__":
    sentences = [
         "今天，刘志军案的关键人物,山西女商人丁书苗在市二中院出庭受审。",
          "江西省监狱管理局与中国太平洋财产保险股份有限公司南昌中心支公司保险合同纠纷案",
          "新北商贸有限公司",]
    demo_NShort_segment(sentences)