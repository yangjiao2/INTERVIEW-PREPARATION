class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        t_ctr = Counter(t)
        missing = len(t_ctr)
        l = 0
        ranges = [l, math.inf]

        for r, c in enumerate(s):
            if c in t_ctr:
                t_ctr[c] -= 1
                if t_ctr[c] == 0:
                    missing -= 1
            # print (r, c, t_ctr, missing)
            while missing == 0 and l <= r:
                c2 = s[l]
                if c2 in t_ctr:
                    t_ctr[c2] += 1
                    if t_ctr[c2] > 0:
                        missing += 1

                if ranges[1] - ranges[0] > r - l:
                    string = [l, r + 1]
                l += 1
                # print ('l', l)


        return s[ranges[0]: ranges[1]] if string[1] != math.inf  else ""


class Solution(object):
    def minWindow(self, search_string, target):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_letter_counts = collections.Counter(target)
        start = 0
        end = 0
        min_window = ""
        target_len = len(target)

        for end in range(len(search_string)):
			# If we see a target letter, decrease the total target letter count
			if target_letter_counts[search_string[end]] > 0:
                target_len -= 1

            # Decrease the letter count for the current letter
			# If the letter is not a target letter, the count just becomes -ve
			target_letter_counts[search_string[end]] -= 1

			# If all letters in the target are found:
            while target_len == 0:
                window_len = end - start + 1
                if not min_window or window_len < len(min_window):
					# Note the new minimum window
                    min_window = search_string[start : end + 1]

				# Increase the letter count of the current letter
                target_letter_counts[search_string[start]] += 1

				# If all target letters have been seen and now, a target letter is seen with count > 0
				# Increase the target length to be found. This will break out of the loop
                if target_letter_counts[search_string[start]] > 0:
                    target_len += 1

                start+=1

        return min_window
