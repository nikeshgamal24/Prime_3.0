is_present = False
word = "Python"
with open("sample.txt","r") as f:
    lines = f.readlines()
    for counter, line in enumerate(lines):
        if word in line:
            is_present = True
            break
    if is_present:
        print(f"{word} word is present in the file in line number {counter+1}")
    else:
        print(f"{word} word is not present in the file")

