import fun
def main(req):
    choice = int(req['instances'][0]['choice'])
    first_num = req['instances'][0]['firstNum']
    second_num = req['instances'][0]['secondNum']
    
    if choice == 1:
        res = fun.sumTwoNum(first_num, second_num)
        return res, "sum"
        
    elif choice == 2:
        res = fun.mulTwoNum(first_num, second_num)
        return res, "mul"
        
    elif choice == 3:
        res = fun.diffTwoNum(first_num, second_num)
        return res, "diff"
        
    else:
        res = "Wrong input"
        return res, "invalid"