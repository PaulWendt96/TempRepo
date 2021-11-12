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


def interpolate_movements(keys, values, interpolate_key, interpolate_meth=None):
    """ value interpolation. the basic idea is this:
    
        keys is a iterable of keys. assume
        keys can be compared with comparison
        operators and manipulated with arithmetic operators
        
        value is an iterable of values. assume 
        values can be manipulated with arithemetic operators
        
        sort the keys, and figure out a range for which 
        low_key < interpolate_key < high_key. 
        
        perform the interpolation based on the values associated
        with low_key and high_key. default is linear interpolation

        ex: 
            periods = [x for x in range(10)]
            price = [0, 10, 20, 5, 8, 12, 15, 2, 6, 17]

            interpolate_movements(periods, price, -0.00001) -> ValueError
            interpolate_movements(periods, price, 0) -> 0
            interpolate_movements(periods, price, 2.5) -> 12.5
            interpolate_movements(periods, price, 6.5) -> 8.5
            interpolate_movements(periods, price, 8.99999) -> 16.99989
            interpolate_movements(periods, price, 9) -> 17
            interpolate_movements(periods, price, 9.00001) -> ValueError
        """
    
    def linear(x_lower, y_lower, x_higher, y_higher, t):
        proportion = (t - x_lower) / (x_higher - x_lower)
        return y_lower + (y_higher - y_lower) * proportion
    
    def pairwise(iterable):
        higher = iter(iterable)
        next(higher)
        return zip(iterable, higher)

    lookup = dict(zip(keys, values))
    sorted_keys = sorted(lookup.keys())
    
    if interpolate_key < min(sorted_keys):
        raise ValueError("Error -- interpolate_key < min")
    elif interpolate_key > max(sorted_keys):
        raise ValueError("Error -- interpolate_key > max")
    
    if interpolate_key in sorted_keys:
        return lookup[interpolate_key]
    
    pairs = pairwise(sorted_keys)
    for low_key, high_key in pairs:
        if low_key < interpolate_key < high_key:
            interpolate = linear if not interpolate_meth else interpolate_meth
            return interpolate(low_key, lookup[low_key],
                               high_key, lookup[high_key],
                               interpolate_key)

        
    raise ValueError("Interpolation failed")  # should never be reached
