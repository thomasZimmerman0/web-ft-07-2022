let fun = (e)=>{

}

let buttons = document.querySelector('.buttons')

const ops = {
    '+': function(a, b) { return a + b },
    '-': function(a, b) { return a - b },
    '*': function(a, b) { return a * b },
    '/': function(a, b) { return a / b },
    };


let x = ''

let y = ''

let op = ''

let hitOperator = false



buttons.addEventListener('click', e=>{
    
    let number = e.target
    if(number.innerText.length == 1){
        input.append(number.innerText)
        }

    if(e.target.id == 'clear'){
        input.innerText = ""
    }

    if(e.target.parentNode.className == 'operators'){
        

        x = input.innerText.slice(0,input.innerText.length  -1)

        op = input.innerText.slice(input.innerText.length -1,input.innerText.length)

        input.innerText = ""
        
    }


    else if(e.target.className == 'equal'){


    y = input.innerText.slice(0,input.innerText.length -1)

    x = parseFloat(x)
    y = parseFloat(y)

    input.innerText = ops[op](x, y)

    x = ''
    y = ''

    }


})