def f1(x: bool, y: bool, z: bool) -> bool:
    f = (not z and x) or (z and y)
    return f
