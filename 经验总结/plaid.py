
# credit history, 問題就是design a system which can calculate the credit history？這樣是不是就是read > write 然後注重db怎麽存，怎麽scale好像想不出來啥特別的，感覺availability 和 consistency 沒那麽重要，

# central bank的

# transaction

# credit history 系统设计 感觉和脸家系统设计的风格差不多 就是画图呗 常见的什么 nosql + kafka + stream processing 甩上去就差不多啦 

# 以前batch processing 经常被拿来纠正stream processing的错误 实际上很多时候batch processing自己的误差也挺大的。现在的stream processing因为stateful的原因 是可以支持很高的正确率的。 

# read heavey write heavy是可以在面试的时候问的 我记得我问啦update和查询都是什么情况下用 又是怎么用 根据具体api的定义还是比较好推断的
# 我用stream是因为这个系统还要支持monitor 个什么东西， 出现变化大于某个值就要发notification什么的 db change stream  + stream process之前工作见挺多

# consistency, payment schema


# 1 跟面试官clarify题目意思，确保双方on the same page
# 2 做之前一定要清楚地communicate自己的思路再做，不然即使答案对了也是一个huge red flag
#    如果时间允许，提出一些alternatives，各个alternatives的trade off，捎带展示一下数据结构知识
# 3 把题目都做完，有的时候会有2到3道。如果做到最后一道，但是做地比较迷糊没做完之类的，就比较危险，碰到比较严格的面试官大概率是不会过
# 4 做完之后主动写test cases，各种情况的正面反面test case都要cover


# central bank 面试官建议iterate只要involve的银行就可以作为central bank，直到它被清零


# https://www.1point3acres.com/bbs/thread-802961-1-1.html

# https://leetcode.com/discuss/interview-question/1367137/plaid-phone-interview


# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
transac = [
  ("Netflix", 9.99, 0),
  ("Netflix", 9.99, 10),
  ("Netflix", 9.99, 20),
  ("Netflix", 9.99, 30),
  ("Amazon", 27.12, 32),
  ("Sprint", 50.11, 45),
  ("Sprint", 50.11, 55),
  ("Sprint", 50.11, 65),
  ("Sprint", 60.13, 77),
  ("Netflix", 9.99, 50),
]

# corner case: days are increasing? positive intege?


from collections import defaultdict

def sol(transac):
    trans = defaultdict(lambda: defaultdict(list))
    
    for comp, amount, ts in transac:
        trans[comp][amount].append(ts)
    res = []
    print (trans)
    for comp, amount_dict in trans.items():
        print (amount_dict)
        for amount, ts in amount_dict.items():
            if len(ts) > 1:
                mid = 1
                while (mid < len(ts) - 1):
                    if ts[mid - 1] + ts[mid + 1] == 2 * ts[mid]:
                        res.append(comp)
                        break
                    
    print (res)


        
sol(transac)
        
#  amount 的最大值和最小值相差不超过20%



from collections import defaultdict
def simplify_transactions(orig_transactions, cent_bank):
    flow_map = defaultdict(int) # dict{ bank : $ flow in, negative means expense}
    res = []
    # step 1: process and populate flow_map, clearing house
    for tran in orig_transactions:
        payer, payee, amount = tran[0], tran[1], int(tran[2:])
        flow_map[payee] += amount if payee != cent_bank else 0
        flow_map[payer] -= amount if payer != cent_bank else 0
    # step 2: output
    for bank, amount in flow_map.items():
        if amount > 0:
            res.append(cent_bank + bank + str(amount))
        elif amount < 0:
            res.append(bank + cent_bank + str(-amount))
    return res

print (simplify_transactions(["AB1", "AC1", "AD1", "AE1", "DE1000"] , 'A'))

print (simplify_transactions(["AB1", "AC1", "AD1", "AE1", "DE1000"] , 'E'))

# 最少的，number of transactions

        
        
class Solution:
  def minTransfers(self, transactions: List[List[int]]) -> int:
    balance = [0] * 21

    for u, v, amount in transactions:
      balance[u] -= amount
      balance[v] += amount

    debt = [b for b in balance if b]

    def dfs(s: int) -> int:
      while s < len(debt) and not debt[s]:
        s += 1
      if s == len(debt):
        return 0

      ans = math.inf

      for i in range(s + 1, len(debt)):
        if debt[i] * debt[s] < 0:
          debt[i] += debt[s]  # debt[s] is settled
          ans = min(ans, 1 + dfs(s + 1))
          debt[i] -= debt[s]  # Backtrack

      return ans

    return dfs(0)
