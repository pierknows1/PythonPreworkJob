value = 7 / 3
# 1. Use the variable above to print this
# expected output:
#
# Value: 2.3333333333333335
# Two decimals: 2.33
# Percent, one decimal: 233.3%
print(f'total:{value}')


red = "red"
blue = "blue"
yellow = "yellow"

print(f'-----------------------------------')
print(f'|{red:^10}|{blue:^10}|{yellow:^10}|')
print(f'|{red:<10}|{blue:^10}|{yellow:>10}|')
print(f'|{red:^10}|{blue:^10}|{yellow:^10}|')
print(f'-----------------------------------')
# 2. Use the three variables above to print this
# expected output:
#
# ----------------------------------
# |       red|      blue|    yellow|
# |red       |blue      |yellow    |
# |   red    |   blue   |  yellow  |
# ----------------------------------
