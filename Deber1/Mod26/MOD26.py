import codecs
def rot131(TEXTO_CIFRADO):
    salida=""
    alfabeto="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in TEXTO_CIFRADO:
        if i in alfabeto:
            salida += alfabeto[(alfabeto.find(i)+13)%26]
        else:
            salida +=1
        return salida
    
mensaje="cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
MOD26=rot131(mensaje)


salida2=codecs.encode(mensaje, "rot-13")
print (salida2)