
def parse_var(var):
    meme = ""
    count = 0
    for i in range(len(var)):
        if i%2 == 0:
            meme += str(count)*int(var[i])
            count += 1
        else:
            meme += "."*int(var[i])
    return meme

def find_and_replace(meme):
    l ,r = 0, len(meme) - 1
    meme = list(meme)

    while l < r:
        while l < len(meme) and meme[l] != ".":
            l += 1
        while r >= 0 and meme[r] == ".":
            r -= 1
        
        if l < r:
            meme[l], meme[r] = meme[r], meme[l]
            l += 1
            r -= 1
    return meme

print(sum(i * int(x) if x != "." else 0 for i, x in enumerate(''.join(find_and_replace(parse_var(input()))))))
