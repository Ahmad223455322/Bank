from model import db, Customer,Account,Transaction
def sortering_transaktionerbild(sortColumn,sortOrder):
   
    allaPersoner = Transaction.query


    if sortColumn == "ID":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.Id.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.Id.asc())

    if sortColumn == "Typ":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.Type.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.Type.asc())

    
    if sortColumn == "Operation":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.Operation.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.Operation.asc())
         
    
    if sortColumn == "Datum":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.Date.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.Date.asc())
    
    if sortColumn == "Amount":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.Amount.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.Amount.asc())
    
    if sortColumn == "NewBalance":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.NewBalance.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.NewBalance.asc())
    
    if sortColumn == "AccountId":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Transaction.AccountId.desc())
        else:
            allaPersoner = allaPersoner.order_by(Transaction.AccountId.asc())                

    return allaPersoner   

def sortering_kontobild(sortColumn,sortOrder):
   
    allaPersoner = Account.query


    if sortColumn == "ID":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Account.Id.desc())
        else:
            allaPersoner = allaPersoner.order_by(Account.Id.asc())

    if sortColumn == "Kontotyp":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Account.AccountType.desc())
        else:
            allaPersoner = allaPersoner.order_by(Account.AccountType.asc())

    
    if sortColumn == "Skapad":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Account.Created.desc())
        else:
            allaPersoner = allaPersoner.order_by(Account.Created.asc())
         
    
    if sortColumn == "Balans":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Account.Balance.desc())
        else:
            allaPersoner = allaPersoner.order_by(Account.Balance.asc())
    
    if sortColumn == "KundID":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Account.CustomerId.desc())
        else:
            allaPersoner = allaPersoner.order_by(Account.CustomerId.asc())
    return allaPersoner    

def sortering_kundbild(sortColumn,sortOrder, page, sök):
    
    allaPersoner = Customer.query.filter(Customer.Id.like(sök) |
                   Customer.GivenName.like('%'+sök+'%')|
                   Customer.City.like('%'+sök+'%'))
  


    if sortColumn == "ID":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Id.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Id.asc())

    if sortColumn == "Förnamn":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.GivenName.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.GivenName.asc())
    

    if sortColumn == "Efternamn":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Surname.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Surname.asc())
         
    
    if sortColumn == "Adress":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Streetaddress.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Streetaddress.asc())
    
    if sortColumn == "Stad":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.City.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.City.asc())
        
    
    if sortColumn == "Land":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Country.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Country.asc())
    
    if sortColumn == "Email":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.EmailAddress.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.EmailAddress.asc())
    
    if sortColumn == "Telefon":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Telephone.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Telephone.asc())


    if sortColumn == "Personnummer":
        if sortOrder == "desc":
            allaPersoner = allaPersoner.order_by(Customer.Birthday.desc())
        else:
            allaPersoner = allaPersoner.order_by(Customer.Birthday.asc())
           
    paginationObject = allaPersoner.paginate(page,50,False)

    return paginationObject
 
 