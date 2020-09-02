print('Hello, world')
print("Hello, world")
print('''
    Hello,
    world
    '''
      )
print("""
    Hello,
    world
    """
      )

text = 'python'
print(text)

# 문자열 반복
print('twice' * 2)  # twicetwice

# 문자열 길이
print(len('hello world'))  # 11

# 문자열 인덱스
print('abcde'[3])  # d

# 문자열 슬라이스 ([인덱스 i: 인덱스 k+1])
print('abcde'[0:3])  # abc

# 문자열 슬라이스 (문자열을 특정 위치 기준으로 나누기)
s1 = '19890204daniel'
left = s1[:8]  # 19890204
right = s1[8:]  # daniel

s2 = 'aaaabbbbbbcc'
segment1 = s2[:4]  # aaaa
segment2 = s2[4:10]  # bbbbbb
segment3 = s2[10:]  # cc

# 문자열 포매팅
name = 'daniel'
print('My name is %s' % name)
