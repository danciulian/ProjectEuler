"""Problem 102"""



def triangarea(x1, y1, x2, y2, x3, y3):
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    area1 = abs((x2 * y3 - x3 * y2) / 2)
    area2 = abs((-x1 * y3 + x3 * y1) / 2)
    area3 = abs((x1 * y2 - x2 * y1) / 2)
    if area == area3 + area2 + area1:
        return True
    else:
        return False


with open('projecteuler.net_resources_documents_0102_triangles.txt') as f:
    my_list = []
    lines = f.readlines()
    for line in lines:
        my_list.append(line)
    counter = 0
    for i in my_list:
        coordinates = list(map(int, i.split(",")))
        x1, y1, x2, y2, x3, y3 = coordinates
        if triangarea(x1, y1, x2, y2, x3, y3):
            counter = counter + 1
    print(counter)