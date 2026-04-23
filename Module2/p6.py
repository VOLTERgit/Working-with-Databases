s = input("Enter string: ")

not_pos = s.find("not")
poor_pos = s.find("poor")

if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
    s = s[:not_pos] + "good" + s[poor_pos+4:]

print(s)