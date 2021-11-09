def applr(**transformations):
    '''
    This is a weird decorator that deserves some explanation

    The basic idea: you can decorate a function with
    @applr(keyword1=transform1, keyword2=transform2, ...)


    Before the decorated function is called, all keyword arguments
    will be compared against the transformations dict. If a 
    match is found (e.g. if a keyword argument is represented
    in the dict), the corresponding transform will be applied
    '''
    def inner(f):
        def wrapped(*args, **kwargs):
            for keyword, argument in kwargs.items():
                if keyword in kwargs:
                    applicator = transformations[keyword]
                    kwargs[keyword] = applicator(argument)
                return f(*args, **kwargs)
        return wrapped
    return innter
