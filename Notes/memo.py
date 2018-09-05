import sys
import datetime

try:
    option = sys.argv[1]
except IndexError as e:
    print("메모를 작성하려면 '-a'를 조회하려면 '-v'를 입력하세요 ({})".format(e))

else:
    if option == '-a':
        try:
            memo = sys.argv[2]
        except IndexError as e:
            print("메모내용을 입력하세요.({})".format(e))
        else:
            f = open(u'D:/Notebooks/Notes/메모장.txt', 'a', encoding='UTF8')
            now = datetime.datetime.now()
            nowDate = now.strftime('%Y-%m-%d %H:%M:%S')
            f.write(nowDate)
            f.write('\n')
            f.write(memo)
            f.write('\n')
            f.write('\n')
            f.close()

    elif option == '-v':
        try:
            f = open('메모장.txt', encoding='UTF8')
        except FileNotFoundError as s:
            print("파일을 찾을수 없습니다.({})".format(s))
        else:
            memo = f.read()
            f.close()
            print(memo)

