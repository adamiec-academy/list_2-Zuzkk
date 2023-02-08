def remove_parentheses(text):
    result = ""
    delate_spacebar = False
    is_inside = False
    for letter in text:
        if letter == "(":
            is_inside = True
        elif letter == ")":
            is_inside = False
            delate_spacebar = True
        elif delate_spacebar:
            result = result
            delate_spacebar = False
        elif not delate_spacebar and not is_inside:
            result += letter
    return result
