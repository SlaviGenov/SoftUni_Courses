animal = input()

match animal:
  case "dog":
        print("mammal")
  case "crocodile" | "tortoise" | "snake":
        print("reptile")
  case _:
        print("unknown")

