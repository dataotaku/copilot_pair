from pptx import Presentation
from pptx.util import Inches
import os

# from PIL import Image

# 이미지가 있는 폴더 지정 필요  (이미지 파일만 있어야 함)
img_folder = "c:/Users/unhoc/Documents/copilot_pair/Mana2_Fashion"
# 저장할 폴더 지정 필요
path_dir = "c:/Users/unhoc/Documents/copilot_pair/pptx"
# 저장할 파일명 수정 필요 (확장자 pptx)
ppt_file_name = "Mana2_Fashion.pptx"

# 파워포인트 객체 생성
prs = Presentation()

# A4 용지 크기 (인치)
a4_width_inch = 8.27  # 8.27 21cm
a4_height_inch = 11.69  # 11.69 29.7cm

# 폴더 내의 모든 파일 순회
prs.slide_width = Inches(a4_width_inch)
prs.slide_height = Inches(a4_height_inch)

# 이미지 파일명 리스트
img_files = os.listdir(img_folder)

# 이미지 파일명의 역순으로 슬라이드 추가
# 리턴 값이 없이 리스트를 역순으로 정렬하여 수정됨.
img_files.reverse()

for img_name in img_files:
    img_path = os.path.join(img_folder, img_name)
    if os.path.isfile(img_path):
        # 이미지 열기
        picture_path = str(os.path.join(img_folder, img_name)).replace("\\", "/")
        # 새 슬라이드 추가 (빈 슬라이드)
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        # 이미지 추가
        left = Inches(0)
        top = Inches(0)
        slide.shapes.add_picture(picture_path, left, top)

        # 새 슬라이드 추가 (빈 슬라이드)
        blank_slide_layout = prs.slide_layouts[6]
        slide = prs.slides.add_slide(blank_slide_layout)

        # 동일 이미지  페이지 추가
        left = Inches(0)
        top = Inches(0)

        slide.shapes.add_picture(picture_path, left, top)


# 파일 저장
prs.save(os.path.join(path_dir, ppt_file_name))

# if __name__ == "__main__":
#     main()

# # resize and attatch
# img_path = os.path.join(img_folder, img_files[0])
# img = Image.open(img_path)
# new_size = (1100, 825)  # 예시로 변경
# resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
# print(resized_img.size)  # (1100, 825
# # Crop the image before resizing
# # Example: Crop the central part of the image
# left = 250
# upper = 100
# right = left + 720
# lower = upper + 590
# crop_area = (left, upper, right, lower)
# cropped_img = resized_img.crop(crop_area)
# # print(cropped_img.size)  # (110, 155)
# # 변경된 이미지 저장
# cropped_img.save(os.path.join(path_dir, temp_img_path))
# blank_slide_layout = prs.slide_layouts[6]
# slide = prs.slides.add_slide(blank_slide_layout)

# # 이미지 추가
# left = Inches(0)
# top = Inches(0)
# slide.shapes.add_picture(str(os.path.join(path_dir, temp_img_path)), left, top)

# prs.save(os.path.join(path_dir, "test_presentation.pptx"))

# for img_name in img_files:
#     img_path = os.path.join(img_folder, img_name)
#     if os.path.isfile(img_path):
#         # 이미지 열기
#         with Image.open(img_path) as img:
#             # 원본 이미지 비율 유지하면서 A4 크기에 맞게 조정
#             new_size = (1100, 825)  # 예시로 800x600 픽셀로 변경
#             resized_img = img.resize(new_size)

#             # 변경된 이미지 저장
#             # Crop the image before resizing
#             # Example: Crop the central part of the image
#             left = 250
#             upper = 100
#             right = left + 720
#             lower = upper + 590
#             crop_area = (left, upper, right, lower)
#             cropped_img = resized_img.crop(crop_area)
#             # print(cropped_img.size)  # (110, 155)
#             # 변경된 이미지 저장
#             cropped_img.save(os.path.join(path_dir, temp_img_path))

#             # 조정된 이미지 저장 (임시 파일)

#             # 새 슬라이드 추가 (빈 슬라이드)
#             blank_slide_layout = prs.slide_layouts[6]
#             slide = prs.slides.add_slide(blank_slide_layout)

#             # 이미지 추가
#             left = Inches(0)
#             top = Inches(0)
#             slide.shapes.add_picture(os.path.join(path_dir, temp_img_path), left, top)

#             os.remove(os.path.join(path_dir, temp_img_path))


# # 파일 저장
# prs.save(os.path.join(path_dir, "test_presentation.pptx"))
