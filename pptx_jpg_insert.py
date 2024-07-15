from pptx import Presentation
from pptx.util import Inches

# # Presentation 객체 생성
prs = Presentation()

# 사용자 정의 용지 크기 설정 (A4 용지 가로 11.69인치, 세로 8.27인치)
prs.slide_width = Inches(11.69)
prs.slide_height = Inches(8.27)

# for lo in prs.slide_layouts:
#     print(lo.name)

# Blank 슬라이드 레이아웃 가져오기
blank_slide_layout = prs.slide_layouts[6]

# 슬라이드 추가
slide = prs.slides.add_slide(blank_slide_layout)

# 제목과 부제목 설정
# title = slide.shapes.title
# subtitle = slide.placeholders[1]

# title.text = "Hello, python-pptx!"
# subtitle.text = "python-pptx 라이브러리를 사용하여 PowerPoint 파일을 생성합니다."

# 새 슬라이드 추가 (빈 슬라이드)
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

# 이미지 추가
img_path = "path/to/image.jpg"
left = Inches(2)
top = Inches(2)
slide.shapes.add_picture(img_path, left, top)

path_dir = "c:/Users/unhoc/Documents/copilot_pair/pptx"
# 파일 저장
prs.save(path_dir + "test_presentation.pptx")
