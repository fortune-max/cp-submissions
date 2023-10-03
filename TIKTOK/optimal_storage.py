from string import ascii_lowercase
txt = list(input())
max_ops = int(input())

curr_idx = 0
is_reduced = { k: False for k in ascii_lowercase }

def get_prev_letter(c):
    if c == 'a':
        return 'z'
    return chr(ord(c) - 1)

while curr_idx < len(txt):
    if txt[curr_idx] == 'a':
        curr_idx += 1
        continue
    while txt[curr_idx] != 'a':
        if is_reduced[txt[curr_idx]]:
            txt[curr_idx] = get_prev_letter(txt[curr_idx])
        elif max_ops > 0:
            max_ops -= 1
            is_reduced[txt[curr_idx]] = True
            txt[curr_idx] = get_prev_letter(txt[curr_idx])

        if txt[curr_idx] == 'a' or (max_ops == 0 and not is_reduced[txt[curr_idx]]):
            curr_idx += 1
            break

print(''.join(txt))
