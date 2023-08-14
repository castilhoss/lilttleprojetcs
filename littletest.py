import pyautogui as mouse 

print("-=="*15)
print("Muzica !")
print("-=="*15)

def main():
    namemusic = str(input("Digite o nome da música que você quer ouvir: "))

    print("Escolha a plataforma que você quer usar: \n[ 1 ] Microsoft Edge\n[ 2 ] Google Chrome\n[ 3 ] Sair")
    escolha = int(input("Plataforma: "))

    if escolha == 1:
        edge(namemusic)

    elif escolha == 2:
        chrome(namemusic)

    elif escolha ==3:
        voltar()
    else:
        print("Escolha um comando comando possível!")

def edge(main):
    mouse.click(9,1065, duration=0.5)
    mouse.write('microsoft edge')
    mouse.press('enter')
    mouse.click(303,48, duration=2)
    mouse.write('https://www.youtube.com/')
    mouse.press('space')
    mouse.press('enter')
    mouse.click(688,97, duration=1)
    mouse.write(main)
    mouse.press('enter')
    mouse.click(613,239, duration=2)

def chrome(main):
    mouse.click(9,1065, duration=0.5)
    mouse.write('google chrome')
    mouse.press('enter')
    mouse.click(303,48, duration=2)
    mouse.write('https://www.youtube.com/')
    mouse.press('space')
    mouse.press('enter')
    mouse.click(688,97, duration=3)
    mouse.write(main)
    mouse.press('enter')
    mouse.click(613,239, duration=3)

def voltar():
    return main()

if __name__ == "__main__":
    main()
