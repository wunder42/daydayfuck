log  = console.log

fs = require "fs"

sum = (arr) -> 
    y = 0
    for x in arr
        y += x
    return y

square = (x) -> x * x

sum_ = (arr) -> 
    y = 0
    for x in arr
        y += square x
    return y

diff = (arr) ->
    return (square sum arr) - (sum_ arr)

test_arr = [1..100]
#console.log diff test_arr
#console.log sum_ test_arr
#log test_arr.map square

huiwen = ->
    max_hw = -999999999
    for x in [100..999]
        for y in [100..990]
            if is_huiwen x, y
                max_hw = Math.max max_hw, x * y
    max_hw

is_huiwen = (x, y) ->
    z = (x * y).toString()
    _t = Math.floor z.length / 2
    while _t >= 0
        if z[_t] != z[z.length-_t-1]
            return false
        _t -= 1
    return true       



#tarr = x * y for x in [100..109] for y in [100..109]

#(tarr.filter (x) -> is_huiwen x).reduce (x, y) -> Math.max x, y

#log [1...4]

class B
    constructor: (@name) ->
        do_it(@name)