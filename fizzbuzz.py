
def fizzbuzz():
    a = "";
    for x in range(1, 101, 1):
        if(int(x/3) * 3 == x):
            print("Fizz");
            a = a + "Fizz ";
        else:
            print(x);
            a = a + str(x) + " ";
    return a;
