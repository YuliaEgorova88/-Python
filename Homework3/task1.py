# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Напишитеабв прогабврамму, удаляющую абвиз тексабвта все слова, соабвдержащие'.split(
    ' ')
print(text)
new_text = []
for i in text:
    if 'абв' not in i:
        new_text.append(i)
print(new_text)

print(['абв' not in x for x in text])
