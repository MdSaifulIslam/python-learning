import math_utils

print(math_utils.add(3, 5))
print(math_utils.area_circle(6))
print(math_utils.PI)

from math_utils import add, area_circle

print(add(3, 5))
print(area_circle(6))

import math_utils as mu

print(mu.add(4, 5))
print(mu.sub(7, 16))

import config

print(config.DATABASE["host"])
print(config.DEBUG)


def run_imported():
    print("===========function running=====")
    print(math_utils.add(3, 5))
    print(math_utils.area_circle(6))
    print(area_circle(6))
    print(mu.sub(7, 16))
    print(config.DATABASE["host"])


if __name__ == "__main__":
    run_imported()
