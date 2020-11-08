for i in range(5):
    try:
        print(i/1);
        rg = rage(10);
    except ZeroDivisionError as e:
        print(e,"divide by zero exception occured");
    except NameError as e:
        print("name exception occured");
    finally:
        print("finally is printed always");
		