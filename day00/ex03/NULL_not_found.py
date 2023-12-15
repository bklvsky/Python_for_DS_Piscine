def NULL_not_found(object: any) -> int:
    names = {None: "Nothing", "": "Empty", False: "Fake"}
    obj_type = type(object)
    if object == 0 and obj_type == int:
        name = "Zero"
    # nan never equals itself thats why we can't use it as a dict key
    elif object != object and obj_type == float:
        name = "Cheese"
    elif object not in names:
        print("Type not Found")
        return 1
    else:
        name = names[object]
    print(f"{name}: {object} {obj_type}")
    return 42
