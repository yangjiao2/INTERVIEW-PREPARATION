def generateAbb(word):
   res = []

   def dfs(pos, curStr, count):
      if pos == len(word):
         if count > 0: curStr += str(count)
         res.append(curStr)
         return

      # abbr
      dfs(pos + 1, curStr, count + 1)

      # keep current char
      if count > 0: curStr += str(count)

      dfs(pos + 1, curStr + word[pos] + count)

   dfs(0, "", 0)
   return res



def generateAbb2(word):
   res = [word]

   def dfs(start, string, res):
      if start >= len(string):
         return

      for i in range(start, len(string)):
         for j in range(1, len(string) - i + 1):
            abbr = string[0 : i] + str(j) + string[i+i : ]
            res.append(abbr)
            dfs(i + 1 + len(num), abbr, res)

   dfs(0, word, res)
   return res
