# The Rain Problem

## Problem:
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

Visual representation of the walls [0, 1, 0, 2, 0, 3, 0, 4]
Rainwater retained: 6
![Rainwater](https://github.com/AnthonyArmour/holbertonschool-interview/blob/main/0x00-rain/rainwater1.png)


Visual representation of the walls [2, 0, 0, 4, 0, 0, 1, 0]
Rainwater retained: 6
![Rainwater](https://github.com/AnthonyArmour/holbertonschool-interview/blob/main/0x00-rain/rainwater2.png)

---

## Solution:

### [Rain Function](https://github.com/AnthonyArmour/holbertonschool-interview/blob/main/0x00-rain/0-rain.py "Rain Function")

``` python
#!/usr/bin/python3

rain = __import__('0-rain').rain

if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))
```

```
usr@ubuntu:~/0x00$ ./0_main.py
6
6
```