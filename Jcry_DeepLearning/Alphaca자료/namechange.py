import os

# 폴더 연결해서 리스트에 폴더 제목들 담기
file_path = 'C:/Users/Playdata/Desktop/[원천]소도체_seg_2'
file_names = os.listdir(file_path)

# 잘 불러오는지 test
# print(file_names[:5])

i = 1
for name in file_names:
    # 기존 경로에서 사진이름 하나 뽑음
    src = os.path.join(file_path, name)
    # change name
    cn = 'QC_cow_segmentation_2_' + str(i) + '.jpg'
    # 바꿔줄 새 이름 만들기
    cn = os.path.join(file_path, cn)
    # src를 cn 으로 바꾸기
    os.rename(src, cn)
    i += 1
