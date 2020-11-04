# 721. Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the
first element accounts[i][0] is a name, and the rest of the elements are emails
representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to
the same person if there is some email that is common to both accounts. Note
that even if two accounts have the same name, they may belong to different
people as people could have the same name. A person can have any number of
accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the
first element of each account is the name, and the rest of the elements are
emails in sorted order. The accounts themselves can be returned in any order.

---

To merge all accounts by its name and the list of the emails belong under that
name, we visualize this problem as a graph problem - and perform dfs.

For each account, we enumerate and find all the emails under that account with
dfs. During dfs, we build a complete set of emails by by traversing on the
graph that we have created as a mapping of emails belong to accounts. This is
done so by iterating on the current account and extract the emails. For each
email we find, we add to the set of the emails found thus far and further
recursive dfs on the accounts found by that email as well.

Time complexity is O(n * log(n)) due to sorting of the emails involved.

---

Python:

```python

class Solution:
    def accountsMerge(self, accounts):
        def helper(node):
            if visited[node]:
                return set()
            allEmails = set()
            visited[node] = True
            for email in accounts[i][1:]:
                allEmails.add(email)
                for neigh in emailToAccounts[email]:
                    allEmails |= helper(neigh)
            return allEmails

        emailToAccounts = collections.defaultdict(list)
        for i, info in enumerate(accounts):
            # for each email, we create a neighbour list that shares same email
            for email in accounts[1:]:
                emailToAccounts[email].append(i)
        
        result = list()
        visited = [False for _ in range(len(accounts))]

        for node, info in enumerate(accounts):
            emails = helper(node)
            if emails:
                # name + sorted order of emails
                result.append([info[0]] + sorted(list(emails)))

        return result
```
