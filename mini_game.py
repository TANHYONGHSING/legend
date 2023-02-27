toyota_models = {"Hilux" : "Pickup truck" , "Vios" : "Sedan" , "Supra" : "Sports car" , "Alphard" : "Minivan"}
models = input("Give me one of the Toyota car's models \n")
if models in toyota_models:
    print("You are a Toyota guy")
else:
    print("You don't know about Toyota")