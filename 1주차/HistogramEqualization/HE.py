import numpy as np
import cv2

class HistogramEqualization:
    
    def __init__(self):
            self.image = cv2.imread("HistogramEqualization\sample.jpg", cv2.IMREAD_GRAYSCALE)
            self.width, self.height= self.image.shape[0], self.image.shape[1]
            self.pixel = self.width * self.height                      # 전체 pixel 수 = image 행 * image 열
            self.factor = 255/self.pixel
            self.histogram = np.zeros(256, dtype = np.uint32)          # 0으로 채워진 길이 256 배열 생성
            self.lutable = np.zeros(256, dtype = np.uint8)
            self.newImage = np.zeros((self.width, self.height), dtype = np.uint8)
        
    def makeHistogram(self):                           
        for i in range(self.width):
            for j in range(self.height):
                self.histogram[self.image[i][j]] += 1                  # 모든 픽셀을 돌며 Histogram 채우기

        return self.histogram
    
    def makeLutable(self):                                             # histogram과 전체 pixel 수 인자로 받기
        sum = 0
        
        for j in range(256):
            sum += self.histogram[j]
            self.lutable[j] = round(sum * self.factor)                 # look-up table = 누적합 * (I_max / 전체 pixel 수)의 반올림
        
        return self.lutable
    
    def makeNew(self):                                                 # image와 look-up table인자로 받기
        for i in range(self.width):
            for j in range(self.height):
                self.newImage[i][j] = self.lutable[self.image[i][j]]   # 기존 image값 look-up table과 매치해서 새로운 이미지 만들기
        
        return self.newImage

    def compareimage(self, src):
        cv2.imshow('image', self.image)
        cv2.imshow('newimage', src)                                    # 새로운 이미지 출력
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    
