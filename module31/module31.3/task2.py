import re

text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

result = re.findall(r'\d{2}-\d{2}-\d{4}', text)
print(result)
