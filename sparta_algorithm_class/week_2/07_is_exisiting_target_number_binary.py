finding_target = 3
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    '''
    정렬되지 않은 input list에 대한 이진 탐색
    :param target: 
    :param numbers: 
    :return: 
    '''

    #TODO. step1: 입력값 정렬
    finding_numbers.sort()  # 정렬,

    #TODO. step2: start, end, pivot값 정의
    start = 0
    end = len(numbers)-1
    pivot = (start + end)//2

    #TODO. step3: start<= end로 순회하며, 분기처리
    while(start <= end):
        if pivot == target:
            return True
        elif(pivot > target):
            end = pivot-1
        else:
            start = pivot+1
        #TODO. step4: start, end값의 변동에 대해 pivot값 재정의
        pivot = (start + end)//2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)