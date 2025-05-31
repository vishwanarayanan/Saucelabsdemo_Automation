valid_login =[("standard_user","secret_sauce")]
invalid_login=[("standard_user","wrong_password"),
               ("","secret_sauce"),("standard_user",""),("","") ]
locked_out_user=[("locked_out_user","secret_sauce")]