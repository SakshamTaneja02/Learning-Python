import re

# pattern = "was"
pattern = r"[A-Z]+orem"

text = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry.
   Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
   when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
   It has survived not only five centuries, Forem dorem but also the leap into electronic typesetting, 
   remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
   sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker 
   including versions of Lorem Ipsum.'''

# m = re.search(pattern, text)
# print(m)
m = re.finditer(pattern, text)
for i in m:
    print(i)
    print(text[i.span()[0]:i.span()[1]])
