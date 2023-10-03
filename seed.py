from table_module import Restaurant,Review,Customer,session

#create restaurants
Restaurant1 = Restaurant(name = "Quiver", price = 100)
Restaurant2 = Restaurant(name = "Fish & Chips", price = 50)

#create customer
Customer1 = Customer(first_name = "James", last_name = "Bond")
Customer2 = Customer(first_name = "Mike",last_name = "Tyson")

#create review
Review1 = Review(star_rating = 3, customer = Customer2 ,restaurant= Restaurant1)
Review2 = Review(star_rating = 5,customer=Customer1,restaurant = Restaurant2)

session.add_all([Restaurant1, Restaurant2, Customer1, Customer2, Review1, Review2])
session.commit()