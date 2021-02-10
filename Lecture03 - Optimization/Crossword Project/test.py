domains = {'a':{1,2,3},'b':{1,2,3},'c':{1,2,3}}
variables = ['a','b','c']

s = min(set(len(domains[variable]) for variable in variables))
print(s)