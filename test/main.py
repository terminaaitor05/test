import ppt
import test

def main():
    input("Elige a qué quieres jugar: piedra, papel o tijera 'p', o adivina el número 'n': ")	
    if input == 'p':
        ppt.play()
    else:
        test.play()

# print(main())

if __name__ == "__main__":
    main()