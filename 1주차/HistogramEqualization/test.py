from HE import HistogramEqualization
he = HistogramEqualization()

histogram = he.makeHistogram()           # histogram 생성
lutable = he.makeLutable()               # look-up table 생성
newImage = he.makeNew()                  # 새로운 Image 생성
        
he.compareimage(newImage)                # 이미지 비교 출력
