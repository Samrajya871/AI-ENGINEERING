employees=[
    {"name":"Alice","salary":60000,"department":"AI"},
    {"name":"Bob","salary":45000,"department":"Web"},
    {"name":"Charlie","salary":75000,"department":"AI"},
    {"name":"David","salary":50000,"department":"Cloud"},
    {"name":"Eva","salary":90000,"department":"AI"}
]
filtering = list(filter(lambda x: x=="AI", employees))
print(filtering)