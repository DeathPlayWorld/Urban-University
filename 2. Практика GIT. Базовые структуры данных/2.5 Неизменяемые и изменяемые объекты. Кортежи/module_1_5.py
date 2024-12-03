#2
immutable_var = int(1),float(2.5),bool(True),str("4")
print(immutable_var)
#P.S. I know that I don't need to parse the types every time, but it's more clear this way.

#3
#immutable_var[0] = 2 -> you will have an error as the result of operation. Reason is simple, every data that you keep in the tuple
#is constant, but there is one exception - list inside the tuple. Here is an example:
immutable_var = [1,2,3], 4, 5 #[1,2,3] a list that we can change.
immutable_var[0][1] = 1 #first index is index of tuple and second is of list.
print (immutable_var)

#4
mutable_list = [1,2.5,True,"4"]
mutable_list[0] = 2.5
print(mutable_list)
