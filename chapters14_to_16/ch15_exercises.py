import math

from ch15_classes_and_objects_the_basics import Point, SMS_store

p = Point(4, 11)
q = Point(6, 15)


def distance(point1, point2):
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    return "{:.2f}".format(math.sqrt(dx ** 2 + dy ** 2))

#print(distance(p, q))

#print(q.reflex_x())

#print(p.slope_from_origin())

#print(p.halfway(q))

#print(p.straight_line_points(q))

my_inbox = SMS_store()
my_inbox.add_new_arrival("0400070565", "16:45", "Hey bro. How are you?")
my_inbox.add_new_arrival("0412345012", "10:00", "Why you not reply?")
print(my_inbox.messages)
print(my_inbox.message_count())
print(my_inbox.get_unread_indexes())
print(my_inbox.get_message(0))
my_inbox.delete(0)
print(my_inbox.messages)
my_inbox.clear()
print(my_inbox.messages)