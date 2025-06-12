
def create_batch(instructions):

    ch = 0 

    while ch != 13:

        print("\n1. Push  2. Pop  3. Add  4. Sub  5. Print")
        print("6. JMP  7. JZ  8. Labels  9.Dup 10. NOP  11. Store Var")
        print("12. Load Var  13. Exit\n")

        ch = int(input("\nEnter Your Choice:"))

        match ch:

            case 1:
                val = int(input("\nEnter A Number To Push: "))
                instructions.append(("PUSH",val))
            
            case 2:
                instructions.append(("POP",))

            case 3:
                instructions.append(("ADD",))

            case 4:
                instructions.append(("SUB",))

            case 5:
                instructions.append(("PRINT",))

            case 6:
                label = input("Write Name From Above Lables: ")
                instructions.append(("JMP",label))

            case 7:
                label = input("Write Name From Above Lables: ")
                instructions.append(("JZ",label))

            case 8:
                label = input("Add Your Label In This Index: ")
                instructions.append(label)

            case 9:
                instructions.append(("DUP",))

            case 10:
                instructions.append(("NOP",))

            case 11:
                instructions.append(("LOAD x",))
            
            case 12:
                instructions.append(("Source x"))

    return instructions 