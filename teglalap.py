def main() -> None:

    a = int(input("Kérem a téglalap szélességét:"))
    b = int(input("Kérem a téglalap hosszúságát:"))

    terulet = a*b
    kerulet = 2*a+2*b

    print("A téglalap területe(T):", terulet)
    print("A téglalap kerülete(K):", kerulet)


if __name__ == "__main__":
    main()
