mmr_list = []  # use to store sum up mmr of each node


class newNode():

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


# function to insert element in binary tree
def insert(temp, data):
    if temp.data is None:
        temp.data = data
        return
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(data)
            break
        else:
            q.append(temp.right)

# find mmr of specific node
def find_mmr(node):
    sum_left = sum_right = 0
    if node.left:
        sum_left = find_mmr(node.left)
    if node.right:
        sum_right = find_mmr(node.right)
    return node.data + sum_right + sum_left

def mmr(root, level):
    global mmr_list
    if root is None:
        return False

    if level == 1:
        mmr_list.append(find_mmr(root))
        return True

    left = mmr(root.left, level - 1)
    right = mmr(root.right, level - 1)

    return left or right

# find all mmr of each node by level traversal and then append it to mmr_list
def levelorder_mmr(root):
    level = 1
    while mmr(root, level):
        level = level + 1


power, compare_couple = input("Enter Input : ").split("/")
power = [int(x) for x in power.split(" ")]
compare_couple = compare_couple.split(",")
T = newNode()
for i in power:
    insert(T, i)
levelorder_mmr(T)
print(mmr_list[0])
for i in compare_couple:
    a, b = i.split(" ")
    if mmr_list[int(a)] > mmr_list[int(b)]:
        print("{}>{}".format(a, b))
    elif mmr_list[int(a)] == mmr_list[int(b)]:
        print("{}={}".format(a, b))
    else:
        print("{}<{}".format(a, b))
