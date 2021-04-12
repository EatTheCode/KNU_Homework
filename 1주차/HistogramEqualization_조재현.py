import cv2
import numpy as np

class HE: 
    def makeHistogram(self, image):                           # image 인자로 받기
        width, height= image.shape[0], image.shape[1]
        histogram = np.zeros(256, dtype = np.uint32)          # 0으로 채워진 길이 256 배열 생성
        sum = 0
        for i in range(width):
            for j in range(height):
                histogram[image[i][j]] += 1                   # 모든 픽셀을 돌며 Histogram 채우기

        return histogram
    
    def makeLutable(self, histogram, pixel):                  # histogram과 전체 pixel 수 인자로 받기
        factor = 255 / pixel
        sum = 0
        lutable = np.zeros(256, dtype = np.uint8)
        
        for j in range(256):
            sum += histogram[j]
            lutable[j] = round(sum * factor)                   # look-up table = 누적합 * (I_max / 전체 pixel 수)의 반올림
        
        return lutable
    
    def makeNew(self, image, lutable):                         # image와 look-up table인자로 받기
        width, height = image.shape[0], image.shape[1]
        newImage = np.zeros((width, height), dtype = np.uint8)
        
        for i in range(width):
            for j in range(height):
                newImage[i][j] = lutable[image[i][j]]          # 기존 image값 look-up table과 매치해서 새로운 이미지 만들기
        
        return newImage
    
    def equalization(self, image):                             # image 인자로 받기
        src = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        pixel = src.shape[0] * src.shape[1]                    # 전체 pixel 수 = image 행 * image 열
        histogram = self.makeHistogram(src)                    # histogram 생성
        lutable = self.makeLutable(histogram, pixel)           # look-up table 생성
        newImage = self.makeNew(src, lutable)                  # 새로운 Image 생성
        
        cv2.imshow('input', src)                               # 기존 이미지 출력
        cv2.imshow('HE', newImage)                             # 새로운 이미지 출력
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# 실행 구문
he = HE()
he.equalization("C:\\Users\\Jaehyeon\\Desktop\\sample.jpg")    #개선하고자 하는 이미지dml 경로