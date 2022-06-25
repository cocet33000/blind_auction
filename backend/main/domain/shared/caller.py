import inspect


def get_caller_function_name():
    """呼び出しもとの関数名を取得する

    Returns:
        str: 関数名
    """
    return inspect.stack()[2].function
