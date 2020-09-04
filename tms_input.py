
import pyperclip
import re


while True:
    try:
        a = int(input("Operacao: "))
        if a == 1 :

            input_tms = pyperclip.paste()
            #input_tms = input_tms.split("\r\n")
           # input_tms = ",".join(input_tms)# <<< teste
            input_tms = re.findall('[0-9]\w+', input_tms)
            print (input_tms)
            
    #         print((len(input_tms))-1)
            
    #         input_tms = ",".join(input_tms)
    #         input_tms = input_tms.split("\t")
    #         input_tms = ",".join(input_tms)
    #         input_tms = input_tms.split(",,")
    #         input_tms = ",".join(input_tms)
    #         input_tms = input_tms.split(",,,")
    #         input_tms = ",".join(input_tms)

    #         print (input_tms)

    #         pyperclip.copy(input_tms)
    #     elif a == 0:
    #         pyperclip.copy(input_tms)
        else:
            break
    except  ValueError:
        print("Somente numeros para selecao")

