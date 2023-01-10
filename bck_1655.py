# 1 5 2 10 -99 7 5
# 1
# 1 5 -> 1
# 1 2 5 -> 2
# 1 2 5 10 -> 2
# -99 1 2 5 10 -> 2
# -99 1 2 5 7 10 -> 2
# -99 1 2 5 5 7 10 -> 5

# import sys
# import heapq
# input = sys.stdin.readline

# def heapSort(iterable):
#     h = []
#     result = []
#     #모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, value)
#     #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result


# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# res = heapSort(arr)

# for i in range(n):
#     print(res[i])

# ------------------------------------------------------------
# 예시 1
# 1 5 2 10 -99 7 5

# 예시 2
# 1, -99
 
import heapq
import sys

n = int(sys.stdin.readline())
leftHeap = []   #중간값보다 작은 값,  최대힙
rightHeap = []  #중간값보다 큰 값,    최소힙


list = []
for i in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)    #[-5, -4, -3, -2, -1]
    else:
        heapq.heappush(rightHeap, num)    #[1, 2, 3, 4, 5]

    # rightHeap이 비어있지 않음 + rightHeap[0]번째 숫자보다 leftHeap[0]번째 숫자가 더 크면
    if rightHeap and rightHeap[0] < -leftHeap[0]:  
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)
    
    list.append(-leftHeap[0])

for j in list:
    print(j)
#------------------------------------------------------------------


# rightHeap = []
# leftHeap = [1,2]

# if rightHeap and 1:
#     print("0 and 1")

# if leftHeap and 1:
#     print("1")


# #빈 Strig, Tuple, List => False값을 가짐









#------------------------------------------------------------

#list.sort 활용?

#수를 받을 카운트 입력 받기
#리스트 생성
#수 하나하나 입력받으면서 비교(중앙값 도출)
    # 중앙값 어떻게 도출?
    # 반복할때 마다 리스트에 담기
    # 리스트 정렬(오름차순)

    # 필수조건. 처음 받은 수
        # 그대로 리스트 담기
    # 조건1. 여태 받은 수 개수가 짝수일때
        # 중앙값 두 수 중 더 작은 수 리스트에 담기

    # 조건2. 여태 받은 수 개수가 홀수일때
        # 중앙값 인덱스 구하기
            # 중앙값 인덱스 = 여태 받은 수 개수를 2로 나눈 몫
        #인덱스에 해당되는 값 리스트 담기

#리스트 내용 차례로 출력


# import sys
# n = int(sys.stdin.readline())

# centerList = []
# numberList = []
# for i in range(n):
#     number = int(sys.stdin.readline())
#     numberList.append(number)
#     numberList.sort()

#     if len(numberList) == 1:
#         centerList.append(number)

#     elif len(numberList)%2 == 0:
#         centerIdx = len(numberList)//2
#         if numberList[centerIdx] >= numberList[centerIdx-1]:
#             centerList.append(numberList[centerIdx-1])
#         elif numberList[centerIdx] < numberList[centerIdx-1]:
#             centerList.append(numberList[centerIdx])

#     elif len(numberList)%2 != 0:
#         centerIdx = len(numberList)//2
#         centerList.append(numberList[centerIdx])

# for j in centerList:
#     print(j)