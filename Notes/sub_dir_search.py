import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        #os.listdir() 으로 파일 리스트를 구할수있다 (파일명만 오므로 경로 dirname를 앞에 붙여준다)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            #os.path.join은 디렉터리와 파일명을 이어주는 함수
            ext = os.path.splitext(full_filename)[-1]  # splitext 파일명을 확장자 기준으로 두부분으로 나눈다..
            if os.path.isdir(full_filename): #isdir은  full_filename이 디렉터리인지 파일인지 구분
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    except PermissionError:
        pass



search("D:/")