content = input()
if 'A' in content:
    content = content.replace('B', 'A')
    content = content.replace('C', 'A')
    content = content.replace('D', 'A')
    content = content.replace('F', 'A')
elif 'B' in content:
    content = content.replace('C', 'B')
    content = content.replace('D', 'B')
    content = content.replace('F', 'B')
elif 'C' in content:
    content = content.replace('D', 'C')
    content = content.replace('F', 'C')
else:
    content = 'A' * len(content)

print(content)