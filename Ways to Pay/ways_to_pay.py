# Figure out how many possible combinations of 3 specific coin
# denominations (1, 2, 5) will add up to a given integer.

# Order matters, so [1,2] is distinct from [2,1] despite being equivalent.

# Output should just be the number of combinations.

# Simple example...
# Input: 3
# Combinations: [1,1,1], [1,2], [2,1]
# Output: 3

##################### Attempt 1 #####################
# Initial thoughts...
# The longest any combination will be is equal to the input (using all 1s).
# Each coin can go in a maximum number of `input // denomination` times (floor division).
# As we go through the possible number of any given coin (A), there will be a remainder (remainderA),
# which can be satisfied by a mix of coins B and C.
# For each remainder, there will also be a maximum number of coin B from `remainderA // denominationB`.
# If we let coin C be 1, that nested remainder (remainderB) will be simple to satisfy
# with remainderB units of coin C.
# If 1 is best to use last, then let's assume that 5 should be first.

# So we can build all combinations (unordered at least) with a set of nested loops.
# Outer loop will run `input // 5 + 1` times. The `+ 1` represents combinations without 5 at all.
# Inner loop will run a varying number of times each loop, increasing from `(input % 5) // 2` to `input // 2`.
# Surely, there must be a formula for how many total times the inner loop will run.
# Maybe numbers will help me see it.

# If input is 10, we have `10 // 5 + 1 = 3`, so there will be 3 outer loops...
# The first time through, we don't loop the inner loop at all because 5 goes into 10 cleanly.
# The second time, we have a remainder 5...
# I think we also need to account for not using any 2s, so the inner loop runs `5 // 2 + 1 = 3` times.
# The third time, we have a remainder 10, so the inner loop runs `10 // 2 + 1 = 6` times.

# That example might be misleading because the input works so nicely with 5s. Let's look again with 11...
# Outer loop runs `11 // 5 + 1 = 3` times, so no change there.
# For the first outer loop, we do have a remainder of `11 % 5 = 1`,
# so the inner loop will run `1 // 2 + 1 = 1` time.
# The second time, we have a remainder of 6, so the inner loop runs `6 // 2 + 1 = 4` times.
# The third time, using no 5 coins, we have a remainder of 11, so the loop runes `11 // 2 + 1 = 6` times.

# In our example input of 10, the inner loop ran a total of 9 times, which represents 9 (unordered) combinations.
# However, there's a 10th combination of [5,5] that didn't have to come from the inner loop.
# To doublecheck, here are all of the (unordered) combinations:
# LOOP 1
# 01 = [5,5]

# LOOP 2
# 02 = [5, 2, 2, 1]
# 03 = [5, 2, 1, 1, 1]
# 04 = [5, 1, 1, 1, 1, 1]

# LOOP 3
# 05 = [2, 2, 2, 2, 2]
# 06 = [2, 2, 2, 2, 1, 1]
# 07 = [2, 2, 2, 1, 1, 1, 1]
# 08 = [2, 2, 1, 1, 1, 1, 1, 1]
# 09 = [2, 1, 1, 1, 1, 1, 1, 1, 1]
# 10 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# In our example input of 11, the inner loop ran a total 11 times, which represents 11 (unordered) combinations.
# To doublecheck that we don't have to add 1 in this case, here are all of the (unordered) combinations:
# LOOP 1
# 01 = [5, 5, 1]

# LOOP 2
# 02 = [5, 2, 2, 2]
# 03 = [5, 2, 2, 1, 1]
# 04 = [5, 2, 1, 1, 1, 1]
# 05 = [5, 1, 1, 1, 1, 1, 1]

# LOOP 3
# 06 = [2, 2, 2, 2, 2, 1]
# 07 = [2, 2, 2, 2, 1, 1, 1]
# 08 = [2, 2, 2, 1, 1, 1, 1, 1]
# 09 = [2, 2, 1, 1, 1, 1, 1, 1, 1]
# 10 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 11 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# I'm pretty sure these examples having the same input and output for unordered combinations
# is just a happy accident, but by laying the data out in this way, I can see a pattern...

# Earlier, I established that the max length of a combination is just the input itself,
# but I can also find the max length of any inner loop's combinations:
# `max = input - (5 * the number of fives) + the number of fives`

# From here, I can figure out how many ones that max row has, and by looking in reverse order,
# I can see that all of those ones get folded into twos until there are 0 or 1 ones left.
# First, my count of ones formula: `ones = max - fives`
# And then, my min formula is either `min = ones // 2 + fives` or `min = ones // 2 + 1 + fives` if ones is odd.

# Something I need to be cognizant of is that trying to actually build all of the combinations
# will breakdown very quickly as the input increases, so my hope is that knowing the span of the
# length of the combinations produced by the inner loops will allow me to do some math instead.

# A factorial can give us the total number of non-repeating permutations. In other words, let's say we
# just have [A,B,C]. For the first element in our combination, we have 3 options: A or B or C. After we
# choose A, we can't pick it again, so for the second element, we have 2 options: B or C. Finally we have 1
# option remaining. By multiplying all of those (3 * 2 * 1), we get that we have 6 options. To confirm:
# 1 = [A, B, C]
# 2 = [A, C, B]
# 3 = [B, A, C]
# 4 = [B, C, A]
# 5 = [C, A, B]
# 6 = [C, B, A]

# The good news is that Python's standard library math module has a factorial function, but the bad news is
# that factorials don't care what is in the slots. [1, 1, 1] counts as a single combination in the example
# I was given; however, using a factorial would count it as 6. My number with this method will almost certainly
# be inflated.

##################### Attempt 2 #####################
# There is a brute force method to solving this...

##################### Attempt 3 #####################
# While just using factorials doesn't make sense, I think there's still something there. We don't have to 
# regard each coin as an item in a list to take away. Instead, every time we take away a coin value, it
# reduces the total amount we still have to satisfy. 

# We can follow a similar but different logic. In the [A,B,C] example, using A meant only B and C were
# available for the next choice, but if we use [1,2,5], using a 1 doesn't mean we can't use another 1.
# Instead, it means we have to satisfy `input - 1` using any of [1,2,5]. With a sufficiently large input,
# this could continue for awhile (e.g., trying to satisfy `input - 1 - 1 - 1 - 1 -1`).

# Once we've reached an amount remaining to be satisfied of exactly 0, we can call that a combination.
# In order to find all the combinations, we have to explore every possible path that gets us to 0. We
# can visualize this as a branching tree, using 3 as an example:
#                                             3
#                       -1         |         -2         |        -5
#                        2         |          1         |        (2)
#         -1         |  -2  |  -5  |  -1  |  -2  |  -5  | -----------------
#          1         |   0  |  (3) |   0  |  (1) |  (4) |
#  -1  |  -2  |  -5  | ---- | ---- | ---- | ---- | ---- |
#   0  |  (1) |  (4) |
# ---- | ---- | ---- |

# If we count up all of the 0s, we can see that this evaluates to 3, which matches the example we were given.

# There are two conditions on which we stop evaluating a branch: reaching 0 or reaching a number less than 0.
# It's important to consider those separately once we get to the actual code because 0s will increase our
# count of combinations by 1.