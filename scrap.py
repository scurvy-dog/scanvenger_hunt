for item in values:
  # remove field description into v and value to y
  # print "%s\n" % item
  if not item:
    continue
  if item == "Room: " + str(rm_number):
    print "EURIKA!\n"
    switch = True
  if switch:
    v,y = item.split(':',1)
    # remove leading or trailing white space
    y =y.strip()
    # Append values to list
    x.append(y)
    if not item:
      break

# Send read list back
