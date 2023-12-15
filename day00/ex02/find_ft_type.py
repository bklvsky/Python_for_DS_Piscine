def all_thing_is_obj(object: any) -> int:
    type_names = {
        list: "List",
        set: "Set",
        tuple: "Tuple",
        dict: "Dict",
        str: "is in the kitchen",
    }
    obj_type = type(object)
    if obj_type not in type_names:
        print("Type not found")
    else:
        type_name = type_names[obj_type]
        if obj_type == str:
            type_name = f"{object} {type_name}"
        print(f"{type_name} : {obj_type}")
    return 42
