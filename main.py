import sajat_modul

if __name__ == "__main__":
    print('Udvozollek a Ko-papir-ollo jatekban!')
    jatek = sajat_modul.KoPapirOllo()
    while True:
        jatek.futtatas()
        jatek.pontszam()
        while True:
            continue_prompt = input('\nSzeretnel meg egyet jatszani? (i/n): ').lower()
            if continue_prompt == 'n':
                print("Ezt sajnalattal hallom!")
                exit()
            elif continue_prompt == 'i':
                break
            else:
                print("Helytelen bemeneti adat!\n")
                continue