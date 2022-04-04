import ppt
import test

def main():
    ans = input("Elige a qué quieres jugar: piedra, papel o tijera 'p', o adivina el número 'n': ")	
    if ans == 'p':
        ppt.play()
    else:
        test.guess(10)

# print(main())

if __name__ == "__main__":
  main()
  while input("Wanna play again? 'y'/'n': ") == "y":  
    main()