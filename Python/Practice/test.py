import os

while True:
    userinput = input('>')
    if userinput == 'pwd':
      # print('/'.join(__file__.split('\\')[:-1]))
    elif userinput == 'dir' or userinput == 'ls':
        print(os.listdir(os.getcwd()))
        print('현재 폴더의 폴더와 파일명 출력')
    elif userinput == 'exit':
        print('안녕히가세요.')
        break