#딕셔너리 자료형(Key, Value) -> (순서x, 중복x, 수정o, 삭제o)

#선언
a = {'name':'kim','phone':'01077777777','birth':930910}
b = {0:'Hello World!'}
c = {'arr':[0,1,2,3]}
print(type(a),a)

#출력
# print('a - ', a['name']) #키가 없으면 에러발생
# print('a - ', a.get('name')) #키가 없으면 None
print('c - ', c.get('arr'))

#딕셔너리 추가
a['address'] = 'Suwon'
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

print('a -', a.keys())
print('a -', list(a.keys()))

print('a -', a.values())
print('a -', list(a.values()))

print('a -', a.items())
print('a -', list(a.items())[1])
print('a -', type(list(a.items())[1]))

print('a -', 'name' in a)
print('a -', 'city' in a)
