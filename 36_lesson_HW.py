import re

tel_num = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578, +89999999999'

reg = r'\+?7\d{10}'

print(re.findall(reg, tel_num))
