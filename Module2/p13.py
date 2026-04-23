d = {"a": 3, "b": 1, "c": 2}

asc = dict(sorted(d.items(), key=lambda x: x[1]))
desc = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("Ascending:", asc)
print("Descending:", desc)