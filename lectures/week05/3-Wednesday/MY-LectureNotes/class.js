// const someFun = () => {

//     console.log(`I'm one`);
// }
// console.log('first');

// let a = 0;

// setTimeout(()=>{
//     console.log('second');
// }, 1000)


// a = a + 1
// console.log('third');


// setTimeout(()=>{
    
//     setTimeout(()=>{

//         setTimeout(()=>{

//             console.log('third print statement');
//         })
//         console.log('Second print Statement');
//     }, 1000)
//     console.log('First print statement');
// }, 3000)



const myFirstPromise = new Promise((resolve, reject)=>{

    // we make our asyncronous code 
    setTimeout(()=>{
        console.log('bruh moment');
        if(true){
            resolve('success')
        }
        else{
            reject('error')
        }
    })
})
.then((response)=>{

    console.log(response);
})
.catch((error)=>{
    console.log(error);
})

console.log('yoyoyo');