
def tower_of_hanoi(n, source, target, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, destination, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, destination, target, source)
    
    
n=int(input("Enter number of moves: "))
source=int(input("Enter source tower number: "))
destination=int(input("Enter destination tower number: "))
target=int(input("Enter target tower number: "))


tower_of_hanoi(n,source,target,destination)
