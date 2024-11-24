def decimal_to_binary(k):
    if k == 1:
        return str(1)
    
    moks = k // 2
    
    smaller_output = decimal_to_binary(moks)

    cur_output = str(k%2)

    return smaller_output + cur_output
