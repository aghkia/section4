import pickle #(객체, 텍스트) 직렬화, 역직렬화할 때 사용

bfilename = 'c:/section4/test.bin'
tfilename = 'c:/section4/test.txt'

data1 = 77
data2 = "Hello World!"
data3 = ["car", "apple", "house"]

#바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f)
    pickle.dump(data2, f)
    pickle.dump(data3, f)

#텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.write('\n'.join(data3))
    f.write('\n')


#바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f)
    print(type(b), ' Binary Read1|', b)
    b = pickle.load(f)
    print(type(b), ' Binary Read2|', b)
    b = pickle.load(f)
    print(type(b), 'Binary Read3|', b)

with open(tfilename, 'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read' + str(i) + '|', line, end='')
