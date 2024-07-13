tmp = input().replace('::', ':?:')
compressed_address = [parse for parse in tmp.split(':') if parse]
original_address = []
for parse in compressed_address:
    if parse == '?':
        num_parse = len(compressed_address)
        for _ in range(8 - num_parse + 1):
            original_address.append('0000')
    else:
        if len(parse) < 4:
            parse = (4 - len(parse)) * '0' + parse
        original_address.append(parse)
print(':'.join(original_address))
