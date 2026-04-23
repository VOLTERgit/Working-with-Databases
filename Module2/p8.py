main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

for i in range(len(main_list)):
    if main_list[i:i+len(sub_list)] == sub_list:
        print("Sublist found")
        break
else:
    print("Sublist not found")