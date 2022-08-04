const fib  = (n) => {
    
    sequence = []

    for(let i = 0; i < n; i++ ){

        if(i == 0){

            sequence[i] = 0

        }
        else if(i == 1){

            sequence[i] = 1
        }
        else{
            
            sequence[i] = sequence[i-1] + sequence[i-2]

        }
        
    }
    
    return sequence
}



console.log(fib(10));




let desks = [ { type: 'sitting' }, { type: 'standing' }, { type: 'sitting' }, { type: 'sitting' }, { type: 'standing' } ];

let deskTypes = desks.reduce((prev, curr)=>{

    curr.type == "sitting" ? prev.sitting += 1 : prev.sitting
    curr.type == "standing" ? prev.standing += 1 : prev.standing

    return prev

},{ sitting: 0, standing: 0 })

console.log(deskTypes);