# Examples

d = {1:"one", "cars":["toyota","mazda"], (1,2): 100}
print d['cars']
print d[1]
print d[(1,2)]

# To add a new entry, or update an existing entry
d["hair"] = "short"
# d now looks like this: {(1, 2): 100, 1: 'one', 'hair': 'short', 'cars': ['toyota', 'mazda']}
print d

d2 = {"dan":{"fullname":"Dan T", "Zip": "90210","Fav_cars":['supra','lambo']}}
print d2["dan"]
# To access the sub dictionary item
print d2["dan"]["fullname"]
# To get the last item in the list in Fav_cars
print d2["dan"]["Fav_cars"][-1]
# To add a new key:value to the inner dictionary
d2["dan"]["gender"] = "Male"
print d2
print ''
print ''

inventory = {
    'gold': 500,
    'pouch': ['flint','twine','gemstones'],
    'backpack':['xylophone','dagger','bedroll','bread loaf']
}
# Add a key to the inventory called pocket and assign it a list of items
inventory['pocket'] = ['seashell','strange berry','lint']
# Sort the items in the list stored under the backpack key]
# Use .sort so the values are sorted in place
inventory['backpack'].sort()
# Remove dagger from the list of items stored under the backpack key
# Use .remove because it takes a value and not an offset
inventory['backpack'].remove('dagger')
# Add 50 to the number stored under the gold key
inventory['gold'] += 50
print inventory

# Create a new dictionary called prices with these key value pairs
prices = {"banana":4.0, "apple": 2.0, "orange": 1.5, "pear": 3.0}
stock = {"banana":100, "apple":250, "orange": 300, "pear": 50}

# Create a variable called total and set it to zero.
# Loop through the prices dictionaries.For each key in prices, multiply the number in prices by the number in stock.
# Print that value and then add it to total.
# Finally, outside your loop, print total.
total = 0
for item in prices:
    # Use float to get the full price for multiplication action
    item_total = float(prices[item]) * int(stock[item])
    print item + ": " + str(item_total)
    total += item_total
print str(total)