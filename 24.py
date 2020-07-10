nums=[2,3,3,4]
def combines(nums):
    assert(nums)
    if len(nums) == 1:
        return [(nums[0], [])]
    out = []
    for i in range(1,len(nums)):
        for j in range(i):
            n1 = nums[j]
            n2 = nums[i]
            if nums.index(n1) != j:
                continue
            if nums.index(n2) not in [i,j]:
                continue
            other_nums = nums[:j] + nums[j+1:i] + nums[i+1:]
            options = [
                    (n1+n2, "{}+{}".format(n1, n2)),
                    (n1-n2, "{}-{}".format(n1, n2)),
                    (n2-n1, "{}-{}".format(n2, n1)),
                    (n1*n2, "{}*{}".format(n1, n2)),
                    ]
            if n1 >= 0 and n2 <= 32 and not (n1 == 0 and n2 < 0):
                options.append((n1**n2, "{}^{}".format(n1, n2)))
            if n2 >= 0 and n1 <= 32 and not (n2 == 0 and n1 < 0):
                options.append((n2**n1, "{}^{}".format(n2, n1)))
            if n2 != 0:
                options.append((n1/n2, "{}/{}".format(n1, n2)))
            if n1 != 0:
                options.append((n2/n1, "{}/{}".format(n2, n1)))
            for (n, s) in options:
                assert(n > 0 or n <= 0)
                new_nums = other_nums + [n]
                assert(len(new_nums) == len(nums) - 1)
                results = combines(new_nums)
                for (result, method) in results:
                    p = (result, [s] + method)
                    out.append(p)
    return out

results = combines([2,3,3,4])
for result, method in results:
    if result == 24:
        print(result, method)


            
