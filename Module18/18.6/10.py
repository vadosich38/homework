alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_up = alphabet.upper()
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf ' \
       'jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft \'ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme ' \
       'wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc ' \
       'bu jstug ttvomf sfzpv\' i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ' \
       'ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju\' b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b ' \
       'hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu\'tm pe psfn gp tf"uip'
new_text = ""
decode_text = ""
slash_counter = 3
temp = ""

for symb in text:
    if symb in alphabet:
        new_text += alphabet[alphabet.index(symb)-1]
    elif symb in alphabet_up:
        new_text += alphabet_up[alphabet_up.index(symb)-1]
    else:
        new_text += symb
print("Первая дешифровка:", new_text)

for symb in new_text:
    if symb == " ":
        temp = temp[(len(temp) - slash_counter) % len(temp):] + temp[:(len(temp) - slash_counter) % len(temp)] + symb
        decode_text += temp
        if "/" in temp:
            slash_counter += 1
        temp = ""
    else:
        temp += symb
print("Расшифрованный текст:", decode_text)

