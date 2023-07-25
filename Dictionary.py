##############
#Dictionaries#
##############

#can_changeble
#unorder

#key-value

dictionary = {"REG": "Regression",
              "LOG": "Logistic Reg",
              "CART": "Classification and reg"}

dictionary["REG"]

dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 12],
              "CART": ["SSE", 15]}

dictionary["REG"]


dictionary = {"REG": 10,
              "LOG": 12,
              "CART": 15}

###key value search in dic###
"REG" in dictionary
dictionary.get("REG")

####Change any value#####
dictionary["REG"] = ["YSA", 10]

dictionary.keys()
dictionary.values()

#####change all list value and keys
dictionary.items()
dictionary.update({"REG": 11 })
dictionary
dictionary.update({"TEST": 12})
