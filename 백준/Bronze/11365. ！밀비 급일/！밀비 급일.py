while True:
    secrets = input()
    if secrets == "END":
        break
    print(secrets[::-1])