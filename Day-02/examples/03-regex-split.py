import re

text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

"""
Split result: ['apple', 'banana', 'orange', 'grape']
"""
