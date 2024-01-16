Why do you want to work at NVIDIA?

What do you like most about NVIDIA?

Where do you see yourself in five years from now?

What are your strengths and weaknesses?




Pay special attention to system design questions and put up questions for clarification.





Q2: Design Question:

Create your own Instagram with following features:
- createProfile
- upload image
- Download image(imgId)
- Follow person

Explain with entity, model, ER, class

We will have Central repo to have uploaded image: CDN

Q3) Profile based questions:

-What is ReactJs and NodeJS(Since My profile is not about react, i simply said I don't know)

What is docker and advantage (He wanted detailed explanation on why do we need docker)
What’s is docker container
What is Kabernets and container. What is orchestrastration
docker vs kuberneted containers (why to prefer kubernetes over docker container. Ans - Orchestration)
What’s saga pattern. Explain with example.
What is factory pattern.



----


https://leetcode.com/discuss/interview-question/279913/key-value-store-with-transaction 

KV store

- add, update, delete
- transaction, commit, rollback, count



from typing import *


class KVStore:
    def __init__(self):
        self.stack = [{}]

    def set(self, key: Any, value: Any):
        """O(1)"""
        self.stack[-1][key] = value

    def get(self, key: Any) -> Optional[Any]:
        """O(transaction)"""
        for i in range(len(self.stack) - 1, -1, -1):
            if key in self.stack[i]:
                return self.stack[i][key]

    def begin(self):
        """O(1)"""
        self.stack.append({})

    def commit(self):
        """O(n_keys)"""
        last_dic = self.stack.pop()

        for k, v in last_dic.items():
            self.stack[-1][k] = v

    def rollback(self):
        """O(1)"""
        self.stack.pop()


def test_KVStore():
    kv = KVStore()
    kv.set(1, 3)

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_single_transaction():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4


def test_KVStore_rollback():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)
    assert kv.get(1) == 3
    assert kv.get(2) == 4
    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) is None


def test_KVStore_multiple_begin():
    kv = KVStore()
    kv.set(1, 3)

    kv.begin()
    kv.set(2, 4)

    kv.begin()
    kv.set(3, 5)

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.commit()

    assert kv.get(1) == 3
    assert kv.get(2) == 4
    assert kv.get(3) == 5

    kv.rollback()

    assert kv.get(1) == 3
    assert kv.get(2) == None
    assert kv.get(3) == None