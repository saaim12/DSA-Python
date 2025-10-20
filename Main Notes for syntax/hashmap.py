# ================================
# 🧠 PYTHON HASHMAP CHEATSHEET for LEETCODE
# ================================

# 1️⃣ Create a hashmap
hashmap = {}                        # empty dictionary
hashmap = {'a': 1, 'b': 2}          # with initial values

# 2️⃣ Access / Insert / Update
hashmap['x'] = 10                   # insert new key
hashmap['a'] = 5                    # update existing key
print(hashmap['a'])                 # access value (KeyError if missing)

# 3️⃣ Check if a key exists
if 'a' in hashmap:
    print("Key 'a' exists")

# 4️⃣ Safe access using get()
value = hashmap.get('z', 0)         # returns 0 if 'z' not found
print(value)
print(hashmap)
# 5️⃣ Increment frequency (super common in LeetCode)
nums = [1, 2, 1, 3]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)                         # {1: 2, 2: 1, 3: 1}

# 6️⃣ Iterate over hashmap
for key in freq:
    print("Key:", key, "Value:", freq[key])

for key, value in freq.items():
    print("Key:", key, "Value:", value)

for value in freq.values():
    print("Only value:", value)

# 7️⃣ Delete operations
del freq[2]                         # remove specific key
freq.pop(99, None)                  # safe remove (ignore if not found)
freq.clear()                        # clear all entries

# 8️⃣ Find key with max/min value
test = {'a': 5, 'b': 2, 'c': 7}
max_key = max(test, key=test.get)
min_key = min(test, key=test.get)
print("Max key:", max_key, "→", test[max_key])   # c → 7
print("Min key:", min_key, "→", test[min_key])   # b → 2

# 9️⃣ Using collections.Counter for counting
from collections import Counter
nums = [3, 2, 3, 1, 1, 1]
freq = Counter(nums)
print(freq)                         # Counter({1: 3, 3: 2, 2: 1})
print(freq.most_common(1))          # [(1, 3)] → most common element

# 🔟 Using defaultdict to avoid .get()
from collections import defaultdict
freq = defaultdict(int)
for num in [1, 2, 2, 3]:
    freq[num] += 1
print(freq)                         # defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 1})

# 1️⃣1️⃣ Common LeetCode patterns:

# -- Two Sum
nums = [2, 7, 11, 15]
target = 9
hashmap = {}
for i, num in enumerate(nums):
    if target - num in hashmap:
        print("Two Sum indices:", [hashmap[target - num], i])
        break
    hashmap[num] = i

# -- Majority Element
nums = [3, 2, 3]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
majority = max(freq, key=freq.get)
print("Majority element:", majority)

# -- Anagram Check
s, t = "anagram", "nagaram"
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1
for c in t:
    count[c] = count.get(c, 0) - 1
is_anagram = all(v == 0 for v in count.values())
print("Is anagram:", is_anagram)

# -- Subarray Sum = K
nums = [1, 2, 3]
k = 3
prefix = {0: 1}
count = 0
curr_sum = 0
for num in nums:
    curr_sum += num
    count += prefix.get(curr_sum - k, 0)
    prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
print("Subarrays with sum =", k, "→", count)

# ================================
# END OF FILE
# ================================
