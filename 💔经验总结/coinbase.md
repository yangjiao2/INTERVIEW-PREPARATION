电话：
原题 ：文件系统
VO：
第一天：系统轮
交易系统 怎么和交易所交互 拿price 讨论如果prod怎么办 不太像其他的系统设计。。。
第二天：
manager 项目深挖
代码1: 原题 interleave iterator 老哥人不错 最后多给了几分钟跑完了tests
代码2：原题 transactions followup 写之前先说了思路 然后说可以写 边写边解释 交流的时候 看着同胞兄弟的表情貌似不是他想要的？？不是的话 您倒是说句话啊。。压着线写完 但是没跑test
两天后email rej 在问feedback 感觉hr不太上心 这家练手用的 给需要的朋友share下dp



第一轮 Interleave原题
follow up是给我写的算法简化
follow up都会用getNext hasNext 因为是迭代器

给了一个 list of transactions {{X, Y, 10%} ，{A, Y, 20%}，{Y, W, 15%} ....}, 还有一个list of 各个account 和初始 balance {{X, 100}, {Y, 50} ....}.
然后问最终 transaction 都执行完，每个用户的 balance 是什么(返回一个map）
follow up 1 如果删掉一个 transaction， 重新返回 transaction 都执行完，每个用户的 balance map
follow up 2 执行 roll back，如果一个 transaction 有问题或者要撤销 transaction，如何 roll back 回之前的状态

FIFO，后来问我有啥别的strategy，我就凭我多年的炒股亏钱经验一顿爆讲。
然后问了如果程序跑着跑挂了怎么处理
然后问了如果多个币种怎么处‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌理

第二轮 transaction balance 转钱 原题
A -> B  30% 那题
follow up 删除一次交易

```
from collections import deque
class Transaction:
   
    def __init__(self, date: int, amount: int, price: float, type: str) -> None:
        self.date = date
        self.amount = amount
        self.unit_price = price / amount
        self.type = type
        
    def __str__(self) -> str:
        return "date=" + self.date + ", amount=" + self.amount + ", unit_price=" + self.unit_price
        
def print_sell(buy_transaction, sell_transaction, amount_sold) -> str:
    proceeds = sell_transaction.unit_price * amount_sold
    gain = amount_sold * (sell_transaction.unit_price - buy_transaction.unit_price)
    info = "sell(date=" + str(sell_transaction.date) + ", date_acquire=" + str(buy_transaction.date) + ", amount=" + str(amount_sold) + ", proceeds=" + str(proceeds) + ", gain=" + str(gain)
    print(info)
   
def handle_buy_transaction(positions: deque, transaction: Transaction) -> None:
    positions.append(transaction)

def handle_sell_transaction(positions: deque, transaction: Transaction) -> None:
    if transaction.type != "sell":
        return
   
    sell_amount = transaction.amount
   
    while sell_amount > 0 and len(positions) > 0:
        first_trans = positions[0]
        if first_trans.amount > sell_amount:
            # this transaction has enough amount to sell
            print_sell(first_trans, transaction, sell_amount)
            first_trans.amount = first_trans.amount - sell_amount
            sell_amount = 0  # we don't need to sell anymore
        else:
            # this transaction doesn't have enough amount to sell
            print_sell(first_trans, transaction, first_trans.amount)

            first_trans = positions.popleft()
            sell_amount = sell_amount - first_trans.amount  # we still need to sell
   
def statement(inputs):
    # a queue of all 'buy' transactions
    positions = deque([])
   
    for input in inputs:
        # 1. build transaction
        transaction = Transaction(input["date"], input["amount"], input["price"], input["type"])
        
        # 2. handle transaction
        if input['type'] == "buy":
            handle_buy_transaction(positions, transaction)
        elif input["type"] == "sell":
            handle_sell_transaction(positions, transaction)




inputs = [
    {"date": 1, "amount": 5, "price": 25.0, "type": "buy"},
    {"date": 2, "amount": 20, "price": 60.0, "type": "buy"},
    {"date": 3, "amount": 7, "price": 42.0, "type": "sell"},
    {"date": 4, "amount": 6, "price": 30.0, "type": "sell"},
    {"date": 5, "amount": 5, "price": 25.0, "type": "buy"},
    {"date": 6, "amount": 5, "price": 25.0, "type": "buy"},
]


statement(inputs)



transaction 就是给fee和size，然后给你一个固定总size，要求尽可能的放入transaction使得fee最大。类似背包问题。followup就是transaction会有parent，想用child，就一定要把parent也放进去，这个很麻烦，最后没写完



电面： FileSystem


hm，货币兑换，讨论自己的项目和设计交易平台。
交易平台有很多可以evolve的地方，聊得比较随性。可以主动提一下你觉得每一个场景会遇到什么情况，应该怎么处理， 像是失败交易后是应该reconciler处理还是通知用户作废，还是平台自负盈亏按提交时价格处‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌理之类的。主要是聊天，看面试官对什么方向感兴趣。面试官想要的不是特别复杂，不要overdesign


https://docs.google.com/document/d/1jaEOhNq7FPDCM1rGahGUDc6z7-srSfIRoKu9Re5sBtY/edit



- 文件系统: 给的path不存在时要求throw exception
- interleave list
- transaction‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌(新题，01背包问题但是不让用dp)
- 换汇问题(DFS)
- 买卖交易(最大最小堆)
- 刷题网期起儿(新题)


# BTC

题目本身不难，我也仔细准备了。一个愚蠢的错误是我准备的时候，就认为是计算每天btc的变化，其实是btc每天的余额，所以没有累计，最后结果不对。
我把给的test case 和 期待的答案贴一下，大家准备的时候方便检查。另外，他们手头的答案是json格式的，如果你的答案不是json的话，会看起来不太容易。但是他们并没有一开始就说要json的具体格式。
以下内容需要积分高于 120 您已经可以浏览
data = [
    {"user_id":"1","timestamp":1536987178,"type":"buy","btc":0.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537095561,"type":"buy","btc":1.52,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537121938,"type":"sell","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537229927,"type":"buy","btc":0.03,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537242677,"type":"sell","btc":0.01,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537244060,"type":"buy","btc":2.7,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537275458,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537299582,"type":"sell","btc":0.9,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537424460,"type":"buy","btc":1.8,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"2","timestamp":1537441605,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537491412,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537529720,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537598813,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537620168,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"2","timestamp":1537681809,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"cc"},
    {"user_id":"1","timestamp":1537683845,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"},
    {"user_id":"1","timestamp":1537772265,"type":"buy","btc":1.23,"usd":7256.52,"payment_method":"ach"}
]
   """
     "1": {
        "09/15/2018": {
            "ach_vol": 7256.52,
            "balance": 0.23,
            "cc_vol": 0
        },
        "09/16/2018": {
            "ach_vol": 7256.52,
            "balance": 0.52,
            "cc_vol": 7256.52
        },
        "09/18/2018": {
            "ach_vol": 21769.56,
            "balance": 3.5400000000000005,
            "cc_vol": 7256.52
        },
        "09/22/2018": {
            "ach_vol": 7256.52,
            "balance": 4.7700000000000005,
            "cc_vol": 0
        },
        "09/23/2018": {
            "ach_vol": 7256.52,
            "balance": 6.0,
            "cc_vol": 0
        },
        "09/24/2018": {
            "ach_vol": 7256.52,
            "balance": 7.23,
            "cc_vol": 0
        },
        "avg_daily_btc": 1.9183333333333337,
        "av‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌g_daily_usd": 12094.200000000004
    },
    """