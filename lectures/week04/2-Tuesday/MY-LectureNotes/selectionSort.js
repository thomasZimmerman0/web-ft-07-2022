let array = [34, 22, 10, 10, 19, 17]

for(let i = 0; i < array.length; i++)
{
    let lowest = i;
    for(let j = i +1; j < array.length; j++)
    {
        if(array[j] < array[lowest])
        {
            lowest = j;
        }
    }

    if (lowest != i)
    {
        let tmp = array[i]
        array[i] = array[lowest]
        array[lowest] = tmp

    }
    
}

console.log(array)

