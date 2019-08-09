import constraint

data = {
    'age': 100
}

kk = constraint.Between(1, 50)
flag = kk.validate(data, 'age')

print flag, kk.result()

print constraint.DataType(int).validate(data, 'age')
print constraint.Required().validate(data, 'age')
