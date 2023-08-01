import jwt

encode = jwt.encode({"val": "test"}, "test", algorithm="HS256")
print(encode)
decode = jwt.decode(encode, "test", algorithms=["HS256"])
print(decode)