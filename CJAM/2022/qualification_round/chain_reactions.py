from collections import defaultdict as d

T = int(input())
for t in range(1, T+1):
    ans = 0; n = int(input())
    weights = [0] + list(map(int, input().split()))
    subs = [0] + list(map(int, input().split()))
    child_store_idxes = d(list)
    parent_store = set()
    idx = 1 # 1-idx
    parent_ans = d(lambda: (0, 0))
    for weight, parent in zip(weights[1:], subs[1:]):
        child_store_idxes[parent].append(idx)
        parent_store.add(parent)
        parent_ans[idx] = (weight, 0)
        idx += 1
    for parent in sorted(parent_store, reverse=True):
        if parent == 0:
            continue
        parent_wt = weights[parent]
        children_wts = [parent_ans[z] for z in sorted(child_store_idxes[parent], key=lambda x: parent_ans[x])]
        # tuples pairs below
        first_child = children_wts[0]; other_children = sum([sum(z) for z in children_wts[1:]])
        parent_ans[parent] = (max(first_child[0], parent_wt), first_child[1] + other_children)

    ans = 0
    for idx in child_store_idxes[0]:
        ans += sum(parent_ans[idx])
    print("Case #%d: %d" % (t, ans))
