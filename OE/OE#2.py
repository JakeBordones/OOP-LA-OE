class phone ():
    def __init__(self,phone,model): 
        self.phone = phone
        self.model = model

    def addphone(self):
        dic_phone[self.phone] = self.model

    def delphone(self):
        dic_phone.pop(self.phone)

    def mod(self):
        tr1 = False
        tr2 = False
        dic_phone.pop(self.phone)
        while True:
            mods = input("Modify phone \n1). Phone name \n2). Phone model\n3). Exit\nSelect the number: ")
            if mods == "1":
                p_name = input("Phone name: ")
                tr1 = True
                #dic_phone[p_name] = self.model
            elif mods == "2":
                p_model = input("Phone model: ")
                tr2 = True
                #dic_phone[self.phone] = p_model
            elif mods == "3":
                break
            else:
                print("Invalid")

        if tr1 and not(tr2):
            dic_phone[p_name] = self.model
        elif tr2 and not(tr1):
            dic_phone[self.phone] = p_model
        elif tr1 and tr2:
            dic_phone[p_name] = p_model
        else :
            dic_phone[self.phone] = self.model

        
dic_phone = {
         "vivo" : "y12",
                }

while True:
    user = input("phone brand manager \n1). veiw brand\n2). create brand\n3). delete brand\n4). modify brand\nWrite Exit to Exit\nchoice Namber: ")
    if user == "1":
        for name in dic_phone:
            print(f"\nBrand name: {name} Phone model: {dic_phone[name]}\n")
    elif user == "2":
        p_brand = input("Phone brand: ")
        p_model = input("Phone model: ")
        ph = phone(p_brand,p_model)
        ph.addphone()
        
    elif user == "3":
        p_brand = input("Phone brand to be delete: ")
        if p_brand in dic_phone:
            ph = phone(p_brand,dic_phone[p_brand])
            ph.delphone()
        else:
            print("invalid")
    elif user == "4":
        p_brand = input("Phone brand to be modify: ")
        if p_brand in dic_phone:     
            ph = phone(p_brand,dic_phone[p_brand])
            ph.mod()
        else:
            print("invalid")
    elif user.lower() == "exit":
        break
    else:
        print("invalid")