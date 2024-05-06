def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization
    of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing the serialized attributes of the object.
    """
    json_dict = {}
    for attr_name in dir(obj):
        if not attr_name.startswith("__") and not callable(getattr(obj, attr_name)):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
    return json_dict
