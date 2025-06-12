from executionLoop import execution_loop
from createBatch import create_batch

ch = 0
memory = []
instructions = []
vars = {}

while ch != 4:

    print("\n1.Create Batch  2.Execute  3.Clear Batch  4.Exit")
    ch = int(input("\nEnter You Choice:"))

    match ch:

        case 1:
            instructions = create_batch(instructions)

        case 2:
            memory = execution_loop(instructions,memory,vars)

        case 3:
            memory = []
            print("Batch Cleared")

        case 4:
            print("Exited")
