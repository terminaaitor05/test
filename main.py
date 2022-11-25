import ppt
import test

def main():
    ans = input("Elige a qué quieres jugar: piedra, papel o tijera 'p', o adivina el número 'n': ")	
    if ans == 'p':
        ppt.play()
    elif ans == 'n':
        test.guess(10)
    else:
        break

# print(main())

if __name__ == "__main__":
  main()
  while input("Wanna play again? 'y'/'n': ") == "y":  
    main()
