import arithmatic as ar
import string_ops as s

a=int(input("Enter first Number="))
b=int(input("Enter second number="))

print(f"Addition={ar.add(a,b)}")
print(f"Multiply={ar.multiply(a,b)}")

text=input("Enter the text=")

print(f"Reverse string={s.reverse_string(text)}")
print(f"vowel={s.count_vowels(text)}")