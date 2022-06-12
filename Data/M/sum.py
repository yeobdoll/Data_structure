def sum_range(begin, end, step=1) : #step이 기본값 가짐   디폴트 인수
    sum = 0
    for n in range(begin, end, step) :
        sum += n
    return sum