# 721 Accounts Merge

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

First, we create an hashmap of all emails to associated accounts. Then, we
recursively visit all account and check for all the emails that are associated
while building the set of emails belong under that account. Since sorting is
required at the end, the time complexity should be O(n * log(n)) where n is the
length of the emails.

---

Python:

```python

class Solution:
    def accountsMerge(self, accounts):
        def helper(i):
            if visited[i]:
                return set()
            allEmails = set()
            visited[i] = True
            # visit all neighbours
            for email in accounts[i][1:]:
                allEmails.add(email)
                for account in emailToAccounts[email]:
                    allEmails |= helper(account)
            return allEmails

        emailToAccounts = collections.defaultdict(list)

        for i, account in enumerate(accounts):
            for email in account[1:]:
                emailToAccounts[email].append(i)

        visited = [False] * len(accounts)
        res = list()

        for i, account in enumerate(accounts):
            allEmails = helper(i)
            if allEmails:
                result.append([account[0]] + sorted(list(allEmails)))

        return result
```
