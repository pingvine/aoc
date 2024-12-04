left_list = []
right_list = []

with open('input.txt', 'r') as data_in:
    for pair in data_in:
        first, second = pair.split()
        left_list.append(int(first))
        right_list.append(int(second))

    left_list.sort()
    right_list.sort()

    dist = 0
    sim_score = 0
    
    for left, right in zip(left_list, right_list):
        dist += abs(left-right)
        sim_score += left*right_list.count(left)

    print(dist)
    print(sim_score)