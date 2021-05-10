def main() -> None:

    a = int(input("Kérem a téglalap szélességét:"))
    b = int(input("Kérem a téglalap hosszúságát:"))

    terulet = a*b
    kerulet = 2*a+2*b

    print("A téglalap területe(T):", terulet ("m2"))
    print("A téglalap kerülete(K):", kerulet ("m"))


if __name__ == "__main__":
    main()
