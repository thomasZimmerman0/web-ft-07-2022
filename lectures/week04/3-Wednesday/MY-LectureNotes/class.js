Array.prototype.myMap = function(callBackFunction){
    let arr =[]

    for(let i = 0; i < this.length; i++){

        arr.push(callBackFunction(this[i], i))
       
    }

    return arr
}

let arr = [1,2,3,4,5]

newArr = arr.myMap( (num, idx) => {
   
   return num + idx})

console.log(newArr);


//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


Array.prototype.myFilter = function(callBackFunction){
    let arr = []
    for(let i = 0; i < this.length; i++){
        let result = callBackFunction(this[i])
        if(result == true){
            arr.push(this[i])
        }
    }
    return arr
}

let newArrr = [1, 2, 3, 4, 5]

let yo = newArrr.myFilter((val)=>{

  return val == 5
})

console.log(yo);

Array.prototype.mySome = function(callBackFunction){
    result = false
    for(let i = 0; i < this.length; i++)
    {
       if (callBackFunction(this[i])){
        result = true
       }
    }
    return result
}

let mama = newArrr.mySome((val) =>{

    return val < 1
})

console.log(mama);