# you can write to stdout for debugging purposes, e.g.

```py

coordinates = [1,1,3,4,4,5,2,2]
coordinates2 = [1,1,3,4,5,7,2,2]

def is_overlapped(coordinates_list):
    def get_coordinates(coordinates):
        return coordinates[0:2] + [coordinates[0]+ coordinates[2] , coordinates[1]+ coordinates[3]]
    rect1 = get_coordinates(coordinates_list[0:4])
    rect2 = get_coordinates(coordinates_list[4:])

    print("rect1", rect1)
    print("rect2", rect2)

    if ((rect1[0] > rect2[2]) or (rect1[2] < rect2[0])) and ((rect1[3] < rect2[1]) or (rect1[1] > rect2[3])):
        return False
    else:
        return True


print ("coordinates", is_overlapped(coordinates))
print ("coordinates2", is_overlapped(coordinates2) )
```
