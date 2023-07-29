n, m = map(int, input().split())

housesgo = 1
total_distance = 0

destinations = list(map(int, input().split()))

for destination in destinations:
    if housesgo <= destination:
        total_distance += destination - housesgo
    else:
        total_distance += n - housesgo + destination
    housesgo = destination

print(total_distance)