from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import User, Category, Item, Base

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
user1 = User(name="Tester User", email="tester@test.com", picture="https://i.pinimg.com/236x/a0/0c/a5/a00ca558e9e6b3adb0ec874df1e683d9--smiley-faces-emoticon.jpg")
session.add(user1)
session.commit()

# Items for Soccer category
category1 = Category(user_id=1, name="Soccer")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Two shinguards", description="A pair of shinguards for soccer players of all levels",
                     category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Shinguards", description="Shinguards for junior soccer players",
                     category=category1)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Jersey", description="A generic soccer jersey",
                     category=category1)
session.add(item3)
session.commit()


# Items for Basketball category
category2 = Category(user_id=1, name="Basketball")
session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Basketball Jersey", description="A nice NBA style basketball jersey for all ages",
                     category=category2)
session.add(item1)
session.commit()



print "catalog successfully populated"
