inputs = open("input.txt").read()
buffer = []
for count, char in enumerate(inputs):
    if len(buffer) < 14:
        buffer.append(char)
    elif len(buffer) == 14:
        buffer = buffer[1:]
        buffer.append(char)
    if len(set(buffer)) == 14:
        print(count + 1)
