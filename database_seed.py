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


# Create Users
user1 = User(name="Wile E. Coyote", email="wile.e@test.com", picture="https://upload.wikimedia.org/wikipedia/en/thumb/3/3c/Wile_E._Coyote.svg/200px-Wile_E._Coyote.svg.png")
session.add(user1)
session.commit()


# Category 1: Transport category
category1 = Category(user_id=1, name="Transport")
session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Jet Bike Kit", description="Like a motorcycle, but without the wheels. Travels up to 200mph.",
                     category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Rocket Sled", description="Powered by a spare Saturn-era rocket engine, this sled can accelerate to 300 mph in 5 seconds.",
                     category=category1)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Foot Springs", description="Attach a pair to your feet and put some spring in your step.",
                     category=category1)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Roller Skis", description="Now you can ski wherever you go! Not just on the snow, but everywhere!",
                     category=category1)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Jet-Propelled Pogo-Stick", description="Like a pogo-stick, this one has jet-rocket attachments so that you'll get a much quicker result! Just watch where you're going though.",
                     category=category1)
session.add(item5)
session.commit()


# Category 2: Pest Removal category
category2 = Category(user_id=1, name="Pest Removal")
session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Giant Mouse Trap", description="Traps anything, especially Giant Rats!",
                     category=category2)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Super Bug Spray", description="Guaranteed to work. They won't be back!",
                     category=category2)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Giant Fly Paper", description="Traps anything, especially Giant Flies!",
                     category=category2)
session.add(item3)
session.commit()


# Category 3: Infrastructure Creation category
category3 = Category(user_id=1, name="Infrastructure Creation")
session.add(category3)
session.commit()

item1 = Item(user_id=1, name="Instant Road", description="Lets you roll out an instant road with ease as it makes a good detour trick. Provided that you watch where you're rolling.",
                     category=category3)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Artificial Rock", description="Lets you become like a real rock out in the open.",
                     category=category3)
session.add(item2)
session.commit()


# Category 4: Defense category
category4 = Category(user_id=1, name="Defense")
session.add(category4)
session.commit()

item1 = Item(user_id=1, name="Triple-Strength Battleship Steel Armor Plate", description="Usually it would fend off most objects, but not Road Runners.",
                     category=category4)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Boom-Erang", description="Like a regular boomerang but better. Guaranteed to return.",
                     category=category4)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Indestructo Steel Ball", description="Lets you roll in a ball that's literally indestructable.",
                     category=category4)
session.add(item3)
session.commit()


# Category 5: Disguise category
category5 = Category(user_id=1, name="Disguise")
session.add(category5)
session.commit()

item1 = Item(user_id=1, name="Cactus Costume", description="Disguise yourself as a cactus and scare others.",
                     category=category5)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Artificial Rock", description="Lets you become like a real rock out in the open.",
                     category=category5)
session.add(item2)
session.commit()


# Category 6: Super Nutrition category
category6 = Category(user_id=1, name="Super Nutrition")
session.add(category6)
session.commit()

item1 = Item(user_id=1, name="Super Speed Vitamins", description="Lets you run fast. Super fast.",
                     category=category6)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Earthquake Pills", description="Why wait? Make your own earthquakes. Loads of fun!",
                     category=category6)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Hi-Speed Tonic", description="Contains vitamins R P + M",
                     category=category6)
session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Triple-Strength Fortified Leg Muscle Vitamins", description="Gives your legs the vitamins it needs to run faster than ever before!",
                     category=category6)
session.add(item4)
session.commit()


# Category 7: Just Add Water category
category7 = Category(user_id=1, name="Just Add Water")
session.add(category7)
session.commit()

item1 = Item(user_id=1, name="Tornado Seeds", description="Part of the tornado kit. Contains one thousand seeds.",
                     category=category7)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Dehydrated Boulders", description="Makes instant boulders with just a drop of water.",
                     category=category7)
session.add(item2)
session.commit()

print "Acme catalog successfully populated!!!"
