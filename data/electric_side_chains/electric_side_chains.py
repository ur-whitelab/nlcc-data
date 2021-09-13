arginine = "R"
aspartic_acid = "D"
alanine = "A"


result = True if electric_side_chains(arginine)=="positive" and electric_side_chains(aspartic_acid)=="negative" and electric_side_chains(alanine)=="no e charge" and electric_side_chains(X)=="error" else False