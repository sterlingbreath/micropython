print(int(False))
print(int(True))

print(0)
print(1)
print(int(+1))
print(-1)

print(int('0'))
print(int('+0'))
print(int('-0'))
print(int('1'))
print(int('+1'))
print(int('-1'))
print(int('01'))
print(int('9'))
print(int('10'))
print(int('+10'))
print(int('-10'))
print(int('12'))
print(int('-12'))
print(int('99'))
print(int('100'))
print(int('314'))
print(int(' 314'))
print(int('314 '))
print(int('  \t\t  314  \t\t  '))
print(int('  1  '))
print(int(' -3 '))

print(int('0', 10))
print(int('1', 10))
print(int(' \t 1 \t ', 10))
print(int('11', 10))
print(int('11', 16))
print(int('11', 8))
print(int('11', 2))
print(int('11', 36))
print(int('xyz', 36))
print(int('0o123', 0))
print(int('8388607'))
print(int('0x123', 16))
print(int('0X123', 16))
print(int('0A', 16))
print(int('0o123', 8))
print(int('0O123', 8))
print(int('0123', 8))
print(int('0b100', 2))
print(int('0B100', 2))
print(int('0100', 2))
print(int(' \t 0o12', 8))
print(int('0o12  \t  ', 8))
print(int(b"12", 10))
print(int(b"12"))


def test(value, base):
    try:
        print(int(value, base))
    except ValueError:
        print('ValueError')


test('x', 0)
test('1x', 0)
test('  1x', 0)
test(f'  1{chr(2)}  ', 0)
test('', 0)
test(' ', 0)
test('  \t\t  ', 0)
test('0x', 16)
test('0x', 0)
test('0o', 8)
test('0o', 0)
test('0b', 2)
test('0b', 0)
test('0b2', 2)
test('0o8', 8)
test('0xg', 16)
test('1 1', 16)
test('123', 37)

# check that we don't parse this as a floating point number
print(0x1e+1)

# can't convert list to int
try:
    int([])
except TypeError:
    print("TypeError")
