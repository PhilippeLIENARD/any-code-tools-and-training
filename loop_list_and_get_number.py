test_item_list = ['87' , 'xswy 3' , '548 ab  2' , '50']

def sum_numbers(item_list) :

    list_number = [] # list numers

    for item in item_list : # loop list

        if item.isdigit() : # condition to check if current element is digit

            list_number.append(int(item)) #if true append current element in list_nmber and set type of element as 'int' 

    sum_list_number = sum(list_number) # sum of list in a 'int' variable

    return print(sum_list_number) #return 'int', in print() method to print what de method returns in terminal



#### 

## recursive version elements : method, argument ( input, list to process) , len of input list , first element of input list list , an append(), an int() an pop() and a sum() method , a return value, double condition


def recursive_sum(item_list , list_number = []):


    if len(item_list) > 0 : ### if an list element contains more than zero elements 
 
        if item_list[0].isdigit(): # if element isdigit() is true  ## not requiere : If wou want get multiples int into an element you can add .split() 

            list_number.append(int(item_list[0])) # add element element as 'int' type in list_number list

            item_list.pop(0) # pop(INDEX_OF_ELEMENT) to delete the first element

        else :

            item_list.pop(0) # pop(INDEX_OF_ELEMENT) to del the first element

        recursive_sum(item_list) # call recursive_sum method
    
    else :

        sum_list_number = sum(list_number) 
        
        #return sum_list_number           
        return print(sum_list_number) 



###

def split_sum_numbers(item_list) :

    list_number = [] # list numers

    for item in item_list : # loop list

        for split_item in item.split():
       
            if split_item.isdigit() : # condition to check if current element is digit

                list_number.append(int(split_item)) #if true append current element in list_nmber and set type of element as 'int' 

    sum_list_number = sum(list_number) # sum of list in a 'int' variable

    return print(sum_list_number) #return 'int', in print() method to print what de method returns in terminal

    

#######################
    
#recursive_sum(test_item_list)
#sum_numbers(test_item_list)
    
split_sum_numbers(test_item_list)

