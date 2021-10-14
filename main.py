with open('new_file.txt', 'a', encoding='utf-8') as f:
    while True:
        text = str(input('Введите текст: '))
        f.write(text + '\n')
        if not text:
            break
f = open('new_file.txt', 'r', encoding='utf-8')
content = f.readlines()
print(content)
f.close()

f = open('new_file.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
f.close()