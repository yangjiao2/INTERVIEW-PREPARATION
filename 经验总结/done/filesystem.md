# Design and implement an in-memory key value datastore.
# This datastore should be able to support some basic operations such as Get, Set and Delete for string keys and values.


# class Solution():
#     def __init__(self,):
#         self.dic = dict()

#     def get(self,key):
#         return self.dic[key] if key in self.dic else None

#     def set(self,key, value):
#         self.dic[key] = value

#     def delete(self,key):
#         if key in self.dic:
#             del self.dic[key]
#         else:
#             return KeyError("not valid key")

# db = Solution()
# db.set("key1", "val1")
# print(db.get("key1"))               # returns val1
# db.delete("key1")
# print(db.get("key1"))           # return None  =>  error case as key1 is not set
# db.set("key1", "val1")
# db.set("key1", "val2")
# print(db.get("key1"))            # return val2
# print(db.delete("key3"))                # error



# Add support for transactions - Begin, Commit and Rollback.

# A transaction is created with the Begin command and creates a context for the other operations to happen.
# Until the active transaction is committed using the Commit command, those operations do not persist. And, the Rollback command throws away any changes made by those operations in the context of the active transaction.

# Every Begin() will always come with a Commit() or Rollback().

# db.set("key0", "val0")
# db.get("key0")               # returns val0 which is set outside of a transaction
# db.begin()
# db.set("key1", "val1")
# db.get("key1")               # returns val1
# db.commit()
# db.get("key1")              # returns val1

# db.begin()
# db.set("key2", "val2")
# db.get("key2")               # returns val2
# db.rollback()
# db.get("key2")              # error case as key2 is not set




class Solution2():

    def __init__(self,):
        self.dic = dict()
        self.transac = None

    def begin(self):
        self.transac = dict()

    def commit(self):
        if self.transac is not None:
            for k, v in self.transac.items():
                if v == None:
                    del self.dic[k]
                else:
                    self.dic[k] = v

    def rollback(self):
        self.transac = None

    # def get(self,key):
    #     if self.transac is not None:
    #         return self.transac[key] if key in self.transac else None
    #     return self.dic[key] if key in self.dic else None

    def get(self,key):
        if self.transac is not None:
            if key in self.transac:
                return self.transac[key]
            else:
                raise KeyError("key not exist")
        if key in self.dic:
            return self.dic[key]
        raise KeyError("key not exist")

    def set(self, key, value):
        if self.transac is not None:
            self.transac[key] = value
            return
        self.dic[key] = value

    def delete(self,key):
        if self.transac is not None:
            self.transac[key] = None
            return
        if key in self.dic:
            del self.dic[key]
        else:
            raise KeyError("not valid key")

    def printout(self):
        print (self.dic)
        print (self.transac)

db = Solution2()
# db.set("key0", "val0")
# print(db.get("key0"))               # returns val0 which is set outside of a transaction
# print ('---')
# db.begin()
# db.set("key1", "val1")
# print(db.get("key1"))               # returns val1
# db.commit()
# print(db.get("key1"))              # returns val1

# print ('---')
# db.begin()
# db.set("key2", "val2")
# print(db.get("key2"))               # returns val2
# # db.printout()
# db.rollback()
# # db.printout()
# print(db.get("key2"))              # error case as key2 is not set

print(db.get("key2"))  # error

db.set("key3", "val3") #
print(db.get("key3"))  # val4
# db.begin()
# db.set("key3", "val3")
# print(db.get("key3"))  #  val3
# db.delete("key3")      #        delete val3 in trans
# print(db.get("key3"))  #  None
# db.commit()
# print(db.get("key3"))  #  None

# Time complexity:
# commit  O(n)
# set, get, delete O(1)


# How might you add support for nested transactions?

# The newly spawned transaction inherits the variables from its parent transaction and changes made in the context of a child transaction will reflect in the parent transaction as well.

# Once a child transaction is committed, the update will be persistent to the global storage. In other words, it won’t be affected if the parent transaction is rolled back or not.

# Example:

# db.begin()                     # Create a parent transaction
# db.set("key1", "val1")
# db.set("key2", "val2")
# db.begin()                     # Create a child transaction
# db.get("key1")              # returns val1 which is set from parent transaction
# db.set("key1", "val1_child")
# db.commit()                 # Commit child transaction
# db.get("key1")              # returns val1_child which is set from child transaction
# db.get("key2")              # returns val2 which is set from parent transaction
# db.commit()                 # Commit parent transaction
