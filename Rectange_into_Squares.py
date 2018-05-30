def sqInRect(lng, wdth,result=[]):
    local_result = list(a for a in result)
    if lng == wdth and len(local_result) == 0:
        return None
    mod = abs(lng - wdth)
    if mod == 0:
        local_result.append(wdth)
        return local_result
    else:
        local_result.append(min(lng,wdth))
        return sqInRect(min(lng,wdth),mod,local_result)

print(sqInRect(5,3))
print(sqInRect(5,5))
