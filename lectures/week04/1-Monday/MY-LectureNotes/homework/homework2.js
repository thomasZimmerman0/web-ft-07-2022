function printNumbers(num1, num2)
{
    for(i = num1; i <= num2; i++)
        console.log(i)
}

printNumbers(5, 25)

function printSquare(size)
{
    arr = []
    for(i = 0; i < size ; i++)
    {
        arr.push('*')
    }

    newArr = arr.join('')

    for(i = 0; i < size ; i++)
    {
        console.log(newArr)
    }
}

printSquare(5)

