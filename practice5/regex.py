#1
import re

pattern = r"ab*"

text = ["a", "ab", "abb", "ac", "b"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")
    else:
        print(t, "-> No match")
#2
pattern = r"ab{2,3}"

text = ["abb", "abbb", "abbbb", "ab"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")
#3

text = "hello_world test_string Python_test my_variable"

pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, text)

print(matches)
#4
text = "Hello World Python is Amazing"

pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, text)

print(matches)
#5
pattern = r"a.*b"

text = ["ab", "acb", "a123b", "acbd"]

for t in text:
    if re.fullmatch(pattern, t):
        print(t, "-> Match")
#6
text = "Hello, world. Python is great"

result = re.sub(r"[ ,\.]", ":", text)

print(result)
#7
text = "hello_world_example"

components = text.split("_")

camel_case = components[0] + ''.join(word.capitalize() for word in components[1:])

print(camel_case)
#8
text = "HelloWorldPython"

result = re.findall(r"[A-Z][^A-Z]*", text)

print(result)
#9
text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text).strip()

print(result)
#10
text = "helloWorldPython"

result = re.sub(r"([A-Z])", r"_\1", text).lower()

print(result)