
def all_variants(text):
    for i in text:
        yield i
    for j in range(1, len(text)):
        yield text[j-1] + text[j]
    for z in range(1, len(text)-1):
        yield text[z-1] + text[z] + text[z+1]


a = all_variants("ABC")

for q in a:
    print(q)