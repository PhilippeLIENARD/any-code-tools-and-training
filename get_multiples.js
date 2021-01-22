
function intProcess (multiple_x = 3 , multiple_y = 7){
    
    let numberList = [];

    for (i=1 ; i < 100 ; i++){

        
        if (i % multiple_x == 0 && i % multiple_y == 0){

            numberList[i] = '* * * * Multiple of' + multiple_x + '&' + multiple_y  + ' * * * ';
        }
        
        else if (i % multiple_x == 0){
            numberList[i-1] = 'Multiple of' + multiple_x;
        }
        else if (i % multiple_y == 0){
            numberList[i-1] = 'Multiple of' + multiple_y;
        }

        else{
            numberList[i-1] = i
        }


    }   

    return console.log(numberList);
}

// execution
intProcess();
