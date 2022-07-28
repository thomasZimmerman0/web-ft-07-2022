let arr = [45, 34, 23, 76, 34]

arr.forEach( (val)=>{

    console.log(val)
} )

let newArr = arr.map( (val)=>{

    return val * 3
})

console.log(newArr);

let newerArr = arr.filter( val =>{

    return true;
})

console.log(newerArr);