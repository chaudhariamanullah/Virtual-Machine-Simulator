def real_instructions(isntructions):

    i = 0
    labels = {}
    real_instructions_list = []

    while i < len(isntructions):
        if isinstance(isntructions[i],str):
            label = isntructions[i]
            labels[label[:-1]] = i
        else:
            real_instructions_list.append(isntructions[i])
        i += 1

    return labels , real_instructions_list


def execution_loop(instructions,memory,vars):

    labels , real_instructions_li = real_instructions(instructions)

    instructions = []
    instructions = real_instructions_li

    print("Your Batch: ")
    print(instructions)

    i = 0

    while i < len(instructions):

        instruction = instructions[i]
        
        if instruction[0] == "PUSH":
            memory.append(instruction[1])

        if instruction[0] == "POP":
            if len(memory) > 0:
                memory.pop()
            else:
                print("\nPop Operation Failed\n")

        if instruction[0] == "ADD":
            if len(memory) > 1:
                n1 = memory.pop()
                n2 = memory.pop()
                memory.append(n2 + n1)
            else:
                print("\nAdd Operation Failed\n")

        if instruction[0] == "SUB":
            if len(memory) > 1:
                n1 = memory.pop()
                n2 = memory.pop()
                memory.append(n2 - n1)
            else:
                print("\nSub Operation Failed\n")

        if instruction[0] == "PRINT":
            if len(memory) > 0:
                print(memory[-1], flush=True)
            else:
                print("\nEmpty Memory\n", flush=True)

        if instruction[0] == "JMP":
            
            if instruction[1] in labels:
                i = labels[instruction[1]]
                continue
        
        if instruction[0] == "JZ":

            if instruction[1] in labels:

                if memory and memory[-1] == 0:
                    i = labels[instruction[1]]
                    continue

        if instruction[0] == "DUP":
            if len(memory) > 0:
                memory.append(memory[-1])
            else:
                print("\nMemory Is Empty")

        if instructions[0] == "NOP":
            pass

        if instruction[0] == "SOURCE X":
            
            if len(memory) > 0:
                vars["x"] = memory[-1]

        if instruction[0] == "LOAD X":
            
            if "x" in vars:
                memory.append(vars["x"])

        i += 1
    
    return memory