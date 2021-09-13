arginine = "R"
glutamic_acid = "Z"
serine = "S"


result = True if h_donor_acceptor(arginine) == "donor" and h_donor_acceptor(glutamic_acid) == "acceptor" and h_donor_acceptor(serine) == "both" and h_donor_acceptor(X) == "error" else False