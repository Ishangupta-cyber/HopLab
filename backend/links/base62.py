ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

BASE = len(ALPHABET)  
INDEX = {ch: i for i, ch in enumerate(ALPHABET)}   # 'g' -> 16, fast lookup


def encode(num:int)->str:
  if num==0:
    return ALPHABET[0]
  chars=[]
  while num>0:
    num,rem=num//BASE,num%BASE
    chars.append(ALPHABET[rem])
  return ''.join(reversed(chars))


def decode(string:str)->int:
  num=0
  for ch in string:
    num=num*BASE+INDEX[ch]
  return num

