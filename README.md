# GCD Pair Sum

## 📌 Overview

This solution calculates a **GCD pair sum** from an input array by transforming each element using the maximum value seen so far.

For every element in `nums`:

1. Maintain a running maximum `mx`.
2. Calculate `gcd(x, mx)`.
3. Store the result in a new list called `prefix`.
4. Sort the resulting list.
5. Use two pointers to pair the smallest and largest values.
6. Add the GCD of every pair to the final answer.

---

## 🧠 Approach

The algorithm can be divided into two main phases.

### Phase 1 — Build the GCD List

We start with:

```python
mx = 0
prefix = []
```

While traversing the array, we update the maximum value seen so far.

For every element `x`:

```python
if x > mx:
    mx = x

prefix.append(gcd(x, mx))
```

The important part is that `mx` represents the **largest value encountered up to the current position**.

### Example

For:

```text
nums = [3, 6, 2, 8]
```

We get:

| x | Running `mx` | `gcd(x, mx)` |
| - | -----------: | -----------: |
| 3 |            3 |            3 |
| 6 |            6 |            6 |
| 2 |            6 |            2 |
| 8 |            8 |            8 |

Therefore:

```text
prefix = [3, 6, 2, 8]
```

---

## 🔢 Phase 2 — Sort and Pair

After creating the GCD list, we sort it:

```text
Before sorting:
[3, 6, 2, 8]

After sorting:
[2, 3, 6, 8]
```

We then use two pointers:

```text
left  → smallest value
right → largest value
```

The pairs are formed as:

```text
(2, 8)
(3, 6)
```

For each pair, we calculate its GCD:

```text
gcd(2, 8) = 2
gcd(3, 6) = 3
```

Therefore:

```text
answer = 2 + 3
       = 5
```

---

## 🔄 Algorithm Flow

```mermaid
flowchart TD
    A[Start] --> B[Input nums]
    B --> C[Initialize mx = 0]
    C --> D[Initialize prefix = []]
    D --> E[Take next element x]
    E --> F{Is x > mx?}
    F -- Yes --> G[Update mx = x]
    F -- No --> H[Keep current mx]
    G --> I[Calculate gcd x, mx]
    H --> I
    I --> J[Append GCD to prefix]
    J --> K{More elements?}
    K -- Yes --> E
    K -- No --> L[Sort prefix]
    L --> M[Set left = 0]
    M --> N[Set right = n - 1]
    N --> O{left < right?}
    O -- Yes --> P[Calculate gcd prefix[left], prefix[right]]
    P --> Q[Add GCD to ans]
    Q --> R[left++, right--]
    R --> O
    O -- No --> S[Return ans]
```

---

## 👀 Two-Pointer Visualization

After sorting:


prefix = [2, 3, 6, 8]

          left       right
           ↓          ↓
        [ 2,  3,  6,  8 ]
          ↘          ↙
            Pair

gcd(2, 8) = 2


Move both pointers inward:


prefix = [2, 3, 6, 8]

             left  right
               ↓    ↓
             [ 3,  6 ]
               ↘  ↙

gcd(3, 6) = 3


Final result:

2 + 3 = 5




## 💻 Implementation


class Solution(object):
    def gcdPairSum(self, nums):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefix = []
        mx = 0

        # Build the GCD list
        for x in nums:
            if x > mx:
                mx = x

            prefix.append(gcd(x, mx))

        # Sort the generated values
        prefix.sort()

        # Pair smallest with largest
        left = 0
        right = len(prefix) - 1
        ans = 0

        while left < right:
            ans += gcd(prefix[left], prefix[right])
            left += 1
            right -= 1

        return ans




## 🧩 Understanding the `gcd()` Function

The solution uses the **Euclidean Algorithm** to calculate the greatest common divisor.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

For example:


gcd(8, 12)

12 % 8 = 4
8 % 4 = 0

GCD = 4


The loop continues until `b` becomes `0`. At that point, `a` contains the GCD.



## 🧪 Example

### Input


nums = [3, 6, 2, 8]


### Step 1 — Build `prefix`


3 → gcd(3, 3) = 3
6 → gcd(6, 6) = 6
2 → gcd(2, 6) = 2
8 → gcd(8, 8) = 8



prefix = [3, 6, 2, 8]


### Step 2 — Sort


[2, 3, 6, 8]


### Step 3 — Pair


gcd(2, 8) = 2
gcd(3, 6) = 3


### Final Answer


2 + 3 = 5




## ⏱️ Complexity

Let "n" be the number of elements in "nums".

| Operation             |               Complexity |
| --------------------- | -----------------------: |
| Build `prefix`        |               O(n log M) |
| Sort `prefix`         |               O(n log n) |
| Two-pointer traversal |               O(n log M) |
| **Overall**           | **O(n log n + n log M)** |
| Extra Space           |                 **O(n)** |

Where `M` represents the magnitude of the input values.

The dominant operation is sorting, so the solution is generally described as:


Time:  O(n log n)
Space: O(n)



## 🎯 Key Concepts Used

This solution demonstrates several important programming concepts:

• **Euclidean Algorithm** for calculating GCD
• **Running maximum** while traversing an array
• **Array transformation**
• **Sorting**
• **Two-pointer technique**
• **Nested functions in Python**
• **Time and space complexity analysis**

---

## 🚀 Takeaway

The main idea is to transform the original array into a new list of GCD values:


nums
  ↓
Running Maximum
  ↓
gcd(x, mx)
  ↓
prefix
  ↓
Sort
  ↓
Two-Pointer Pairing
  ↓
GCD Sum
  ↓
Answer
```

This approach separates the problem into two clear stages:

**Transform → Sort → Pair → Calculate**
