def join_parametr(*args:dict):
    result={}
    [result.update(arg) for arg in args]
    return result

main_callable = join_parametr