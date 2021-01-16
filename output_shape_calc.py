while(True):
    wh = int(input("Input width/height: "))
    k = int(input("Kernel size: "))
    p = int(input("Padding: "))
    s = int(input("Stride: "))
    print((wh - k + (2 * p)) / s + 1)
    
    c = input("Continue? (y/n): ")
    if c.lower() == 'n':
        break
