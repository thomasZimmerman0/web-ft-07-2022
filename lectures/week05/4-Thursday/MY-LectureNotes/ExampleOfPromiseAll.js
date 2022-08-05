
// Promise.all

let p1 = new Promise((resolve, reject)=>{

    setTimeout(() =>{
        
        resolve(100)
    }, 0)
})

let p2 = new Promise((resolve, reject)=>{
    resolve(1000)
},1000)

let p3 = new Promise((resolve, reject)=>{

    resolve('hello')
}, 500)
        

Promise.all([p1, p2, p3])
.then(dataArr=>{

    console.log(dataArr);

})
        