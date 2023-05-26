toyota_models = {"Hilux" : "Pickup truck" , "Vios" : "Sedan" , "Supra" : "Sports car" , "Alphard" : "Minivan"}
models = input("Give me one of the Toyota car's models \n")
if models in toyota_models:
    print("You know some of the Toyota models.")
else:
    print("You don't know about Toyota.")