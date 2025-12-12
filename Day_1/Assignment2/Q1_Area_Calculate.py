def area_square(l):
    print(f"Area of square : {l*l}")

def area_rectangle(l,b):
    print(f"Area of rectangle : {l*b}")

def area_circle(r):
    print(f"Area of circle : {3.14*r*r}")

def area_triangle(b,h):
    print(f"Area of circle : {0.5*b*h}")

while True:
    print("\nEnter which area you want to calculate:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Exit")

    x = int(input("Enter choice : "))
    match x:
        
        case 1:
            l=int(input("Enter lenght of Square : "))
            area_square(l)

        case 2:
            l=int(input("Enter lenght of Rectangle : "))
            b=int(input("Enter breadth of Rectangle : "))
            area_rectangle(l,b)

        case 3:
            r=int(input("Enter radius of Circle : "))
            area_circle(r)

        case 4:
            b=int(input("Enter Base of Triangle : "))
            h=int(input("Enter Hight of Triangle : "))
            area_triangle(b,h)

        case 5:
            print("Exited program !!!")
            break
                

        case _:
            print("Invalid choice! Please try again.")



