import zlib
with open('bb.idl',"rb") as f:
    buf=f.read()
print(len(buf))
# 압축하기
compressed = zlib.compress(buf)
b=b"#IDLSTART#"+compressed
print(b)

print(len(compressed))
