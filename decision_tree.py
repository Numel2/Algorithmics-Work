def loan(income, criminal, job, credit):
    if income < 30000 and criminal == True:
        return 'loan'
    elif 30000 < income < 70000:
        if job > 5:
            return 'loan'
        elif 1 < job < 5 and credit == True:
            return 'loan'
        else:
            return 'no loan'
    elif income > 70000 and criminal == False:
        return 'loan'
    else:
        return 'no loan'


if __name__ == '__main__':
    print(loan(40000, True, 3, True))