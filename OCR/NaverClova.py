#https://api.ncloud-docs.com/docs/ai-application-service-ocr-ocr#%EC%9A%94%EC%B2%AD-%EB%B0%94%EB%94%94
import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image
from matplotlib import pyplot as plt

import uuid
import json
import time
import cv2
import requests


def plt_imshow(title='image', img=None, figsize=(8, 5)):     #Jupyter Notebook 또는 Colab에서 이미지를 확인하기위한 Function
    plt.figure(figsize=figsize) # matplotlib의 함수 pyplot(=plt) 사용

    if type(img) == list:   #img가 list면  check result에 plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))로 사용됨.
        if type(title) == list:  #title이 리스트면 실행
            titles = title  # titles 에 title 리스트 입력
        else:
            titles = []     #title이 리스트가 아니면 titles는 빈 list로 두기

            for i in range(len(img)):   #img리스트의 길이 만큼 반복
                titles.append(title)     # titles 빈 리스트에 title을 붙여 넣기

        for i in range(len(img)):  #img리스트의 길이만큼 반복
            if len(img[i].shape) <= 2:  #img list의 행렬 차원이 2보다 작으면
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

#OpenCV의  putText 를 이용하여 한글을 출력하는 경우 한글이 깨지는 문제를 해결하기 위한 Funtion
def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
    if type(image) == np.ndarray:   #image 매개변수의 타입이 numpy의 행렬 자료구조 클래스라면
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    #image의 색깔 변환
        image = Image.fromarray(color_coverted)

    if platform.system() == 'Darwin':
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows':
        font = 'malgun.ttf'

    image_font = ImageFont.truetype(font, font_size)   #PIL라이브러리의 함수
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text, font=image_font, fill=color)

    numpy_image = np.array(image)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    return opencv_image
#도메인 생성 시 확인했던 APIGW Invoke URL는 api_url 에 입력하고, Secret Key는 secret_key  값에 입력합니다.

def main():
    api_url = 'https://f2h78xnnlh.apigw.ntruss.com/custom/v1/17592/244210e48437b6556980a70249a99369934a352429034cef9d7bd253b3bf2c01/general'
    secret_key = 'cm5wR0pkSGdwd3V1RlJjbllnc1hjREFwYVpIbWxtQmg='

    #이미지는 바이너리로 변환하여  load 합니다.
    path = 'C:/users/kimjh/ocr_testPict/ocr_test.jpg'
    files = [('file', open(path,'rb'))]

    #REST API 호출 후 응답을 기다립니다.

    request_json = {'images': [{'format': 'jpg',
                                    'name': 'demo'
                                   }],
                        'requestId': str(uuid.uuid4()),
                        'version': 'V2',
                        'timestamp': int(round(time.time() * 1000))
                       }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}  #json.dumps로 파이썬 객체를 json으로 전환한 후 UTF-8(2진수)로 인코딩. 인코딩을 하지 않아도...
    #정상작동 함. json 형식으로 바꿔주는 건 필수인 것 같음.

    headers = {
      'X-OCR-SECRET': secret_key,
    } #네이버 클로바 사이트에 보면 요청 헤더 나와 있음. 이런 종류의 요청할 때는 헤더가 필수인가 봐.

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
    result = response.json()



    #Check Result
    img = cv2.imread(path)
    roi_img = img.copy()
    #클로바 설명 링크 가보면 응답 JSON을 볼 수 있당. 그 응답 중에서 image 아래, 리스트 중 첫번째 객체 딕셔너리 fields가 있음. 그 중 키워드 inferText에 변환 스트링이 담김.
    #그 아래 것들은 변환 결과 사진 띄어주는 코드.
    text_list=[]
    for field in result['images'][0]['fields']:

        text = field['inferText']
        text_list.append(text)

        # vertices_list = field['boundingPoly']['vertices']
        # pts = [tuple(vertice.values()) for vertice in vertices_list]
        # topLeft = [int(_) for _ in pts[0]]
        # topRight = [int(_) for _ in pts[1]]
        # bottomRight = [int(_) for _ in pts[2]]
        # bottomLeft = [int(_) for _ in pts[3]]

        # cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 2)
        # cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 2)
        # cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 2)
        # cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 2)
        # roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)

    return text_list

    #plt_imshow(["Original", "ROI"], [img, roi_img], figsize=(16, 10))

if __name__ == '__main__':
    main()
