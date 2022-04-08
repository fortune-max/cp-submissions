from random import shuffle, randrange


def scramble_string(txt):
    txt = list(txt)
    shuffle(txt)
    return "".join(txt)


def gen_rand_arr(cls, count, upper_lim=None, lower_lim=None):
    ret_val = []
    if cls == int:
        for _ in range(count):
            ret_val.append(randrange(upper_lim or 9))
    if cls == str:
        for _ in range(count):
            if lower_lim and not upper_lim:
                char = chr(randrange(upper_lim))
            elif lower_lim and upper_lim:
                char = chr(randrange(lower_lim, upper_lim))
            else:
                char = chr(randrange(97, 97+26))
            ret_val.append(char)
        ret_val = "".join(ret_val)
    return ret_val
