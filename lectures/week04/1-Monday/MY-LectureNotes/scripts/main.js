// console.log('inside of external js file');

// let firstName = "Tommy";
// let lastName = "Zimmerman";

// console.log(firstName + " " + lastName);

// let a = 4;
// let b = 5;

// let sum = a + b;

// nameSum = firstName.length + lastName.length

// console.log(nameSum)

// let word1 = "hello"
// let word2 = "world"

// let greeting2 = word1 + " " + word2

// hello is it me you're looking for


// let name = firstName + " " + lastName

// console.log(`The start of lastName is at ${name.indexOf('Z')}`)


// if (a == b){
    
//     console.log('you get a free beer!');

// }

// let num1 = 5;
// let num2 = 5;

// write a program that compares the values
// num1 > num2
// num1 is greater than num2 
// i.e 5 is greater than 3

// default

// if(num1 > num2){
//     console.log(`${num1} is greater than ${num2}`)
// }
// else if(num1 < num2){
//     console.log(`${num2} is greater than ${num1}`)
// }
// else if(num1 == num2){
//     console.log(`${num1} is equal to ${num2}`)
// }

// let fruit = "Papayas";

// switch(fruit){

//     case 'Oranges':
//         console.log('Oranges are $0.59 a pound.');
//         break;
       

//     case 'Mangoes':
//         console.log('Mangoes are $0.59 a pound.');
//         break;

//     case 'Papayas':
//         console.log('Papayas are $0.59 a pound.');
//         break;

//     default:
//         console.log('We are out of that fruit')
// }




// let month = 2


let arr = [23, 4, 5, 6]

for( let count = 10 ; count < 10; count++){
     
    console.log(count);

}

for( let i = 0 ; i < 20; i++){
    if (i % 2 == 0){
        
        console.log(i)
    }
}

let i = 0
while(i < 20){
    if (i % 2 == 0){
        
        console.log(i)
    }
    i++
}

for(let i = 0; i <= 30; i++ ){

    if(i % 5 == 0 && i % 3 == 0){

        console.log(i + ' fizz buzz')
    }
    else if (i % 3 == 0){
        console.log(i + ' fizz')
    }
    else if (i % 5 == 0){
        
        console.log(i + ' buzz')
    }
    else{

        console.log(i)
    }
}


let arr1 = [];
let arr2 = [4, 5, 7, 8, 23]

arr2.push(99)

console.log(arr2);


let str = "javascript"

arr = str.split('')

for(i = 0; i < arr.length; i++)
{
    if(i % 2 != 0)
    {
        arr[i] = 'Z'
    }
}

str = arr.join('')

console.log(str)

let myObj = {
    firstName : "Tommy",
    lastName : "Zimmerman"
}


let resut = myObj["firstName"];

result = myObj.lastName;
console.log(result);

myObj.city = "Naples"


delete myObj.firstName

console.log(myObj);
