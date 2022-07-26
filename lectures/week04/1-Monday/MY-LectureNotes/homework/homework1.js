function hello(name) {
  
    if(name == null)
    {
      console.log("Hello World")
    }
    else
    {
      console.log(`Hello ${name}`)
    }
}
  hello();

  function madlib(name, subject)
  {
    string = name + "'s favorite subject in school is " + subject;

    return string;
  }

  sentence = madlib('Anushka', 'art')

  console.log(sentence)

  function tipAmount(bill, svcLvl, pats)
  {
    tip = 0
    total = 0
    splitAmt = 0

    if(svcLvl == 'good')
    {
      tip = bill * .20
    }
    else if(svcLvl == 'fair')
    {
      tip = bill * .15
    }
    else if(svcLvl == 'bad')
    {
      tip = bill * .10
    }

    total = bill + tip
    
    splitAmt = total/pats
    return splitAmt
  }

  console.log(tipAmount(100, 'bad', 3))