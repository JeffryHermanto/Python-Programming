# Stacks

# LIFO
# Last In First Out

browsingSession = []

browsingSession.append(1)
browsingSession.append(2)
browsingSession.append(3)
print(browsingSession)

last = browsingSession.pop()
print(last)
print(browsingSession)

if browsingSession is not []:
    print("Redirect", browsingSession[-1])
