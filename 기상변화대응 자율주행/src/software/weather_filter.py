import os
import cv2
import numpy as np

def foggy_preprocess(image, gamma=1.2):
    """
    CLAHE + Gamma 보정을 적용하는 함수
    :param image: 입력 BGR 이미지
    :param gamma: Gamma 보정 값 (기본 1.2)
    :return: 전처리된 이미지
    """
    # CLAHE: LAB 색 공간으로 변환 후 L 채널에 적용
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    
    # Gamma 보정
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(256)]).astype("uint8")
    result = cv2.LUT(enhanced, table)
    
    return result

# 입력 및 출력 폴더 경로 설정 (Windows 경로, raw-string 사용)
input_folder = r"C:\Users\user\Desktop\graduate\bdd100k\images\s"
output_folder = r"C:\Users\user\Desktop\graduate\bdd100k\images\foggy"

# 출력 폴더가 없으면 생성
os.makedirs(output_folder, exist_ok=True)

# 입력 폴더 내의 모든 이미지 파일 처리
for file in os.listdir(input_folder):
    if file.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(input_folder, file)
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"이미지를 읽을 수 없습니다: {file}")
            continue
        
        # 전처리 적용
        processed_image = foggy_preprocess(image, gamma=1.2)
        
        output_path = os.path.join(output_folder, file)
        cv2.imwrite(output_path, processed_image)
        print(f"처리 완료: {file}")

print("전처리 완료")