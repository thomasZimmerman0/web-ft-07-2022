const uniqSort = function(arr){

    const cache = {};

    newArr = []

    for(let i = 0; i < arr.length; i++ ){

        if(cache[arr[i]] == true){

        }
        else{
            cache[arr[i]] = true
            newArr.push(arr[i])
        }
    }

    return newArr.sort((a,b) => a - b);

};
console.log(uniqSort([4,2,2,3,2,2,2]));

//???????????????????????????????????????????

const cache = {}
const times10 = (n) => n * 10

const memoTimes10 = (n) => {

    if(n in cache){

        console.log('fetching from cache', n);
        return cache[n]
    }
    else{

        console.log('Calculate result');
        cache[n] = times10(n)
        return cache[n]

    }
}

console.log(memoTimes10(9));






const fibo = (n) => {

    let sequence = [0, 1]

    for(let i = 2; i < n; i++){

        let next = sequence[i - 1] + sequence[i - 2]

        sequence.push(next)
    }

    return sequence
}

function memoize(fn){
    const cache = {}
    return function(...args){
      if (cache[args]){
        return cache[args];
      }
      newCall = fn.apply(null, args);
      cache[args] = newCall;
      return newCall;
    }
  }