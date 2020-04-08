import pandas as pds 

germanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 
    'Price': [23845, 171995, 135925 , 71400]
    }

japaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 
    'Price': [29995, 23600, 61500 , 58900]
    }

datafr1 = pds.DataFrame(germanCars)
datafr2 = pds.DataFrame(japaneseCars)

datafr3 = pds.concat([datafr1,datafr2], ignore_index=True)

datafr3.sort_values(by = ['Price'], inplace = True, ignore_index = True)

print(datafr3)

    
    


