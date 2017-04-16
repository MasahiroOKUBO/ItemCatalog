# coding: utf-8

from ItemCatalog.utility import db_session
from ItemCatalog.models import User
from ItemCatalog.models import Category
from ItemCatalog.models import Item

User1 = User(name="TestUser",
             email="TestUser@okubo-tech.com",
             picture='images/guest_user.png')

Category1 = Category(name="second hand",
                     user=User1)

Category2 = Category(name="HandMade",
                     user=User1)

Category3 = Category(name="Premiere",
                     user=User1)

Item1 = Item(
    name="Guiter",
    description="YAMAHA Guiter. NO case box.",
    price="$200",
    picture="images/sample_item1.jpg",
    user=User1,
    category=Category1)

Item2 = Item(
    name="I made Cookie!!",
    description=(
        "I made cookie. very good taste."),
    price="$5",
    picture="images/sample_item2.jpg",
    user=User1,
    category=Category2)

db_session.add(User1)
db_session.add(Category1)
db_session.add(Category2)
db_session.add(Category3)
db_session.add(Item1)
db_session.add(Item2)
db_session.commit()

print "added catalog items!"
