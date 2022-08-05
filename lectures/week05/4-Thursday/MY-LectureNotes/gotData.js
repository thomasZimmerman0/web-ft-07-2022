class Character{
    constructor(name, houseURL, houseName){
        this.name = name
        this.houseURL = houseURL
        this.houseName = houseName

    }
    
}

let characterList = []

let fetchArr = []; //used to accumulate all characters objects

let url = "";
let main = document.querySelector('#main')

for(let page = 0; page < 43; page++){

    url = fetch(`https://www.anapioficeandfire.com/api/characters?page=${page}&pageSize=50`)

    fetchArr.push(url)
}

let promise = Promise.all(fetchArr)

promise.then(resultsArr=>{

    let newArr = resultsArr.map(char =>{
        return char.json()
    })

    return Promise.all(newArr)
})

.then(dataArr =>{
    
    let characterCard = ''

    for(let outter = 0; outter < dataArr.length; outter++){

        for(let inner = 0; inner < dataArr[outter].length; inner ++){

            console.log(dataArr[outter][inner].allegiances);

            char = new Character(dataArr[outter][inner].name, dataArr[outter][inner].allegiances, [])

            characterList.push(char)
        }
    }

    
            for(let index = 0; index < characterList.length; index++){
       
                for(let houses = 0; houses < characterList[index].houseURL.length; houses++){
                    

                    fetch(characterList[index].houseURL[houses])
                    .then(result=>result.json())
                    .then(data=>{
                        
                        
                        characterList[index].houseName.push(data.name)
                        characterCard += `<li>${data.name}</li>`
                        
                        if(characterList[index].name == ""){}
                        
                        else if(houses == 0){
                            
                            main.innerHTML += `
                            
                            <div id="card" class="card1 col-3 showhim">
                                ${characterList[index].name}
                                <ul class="showme houses${index}">
                                    <li>${characterList[index].houseName[houses]}</li>
                                </ul>
                                <button type="button" id="button">More Info!</button>
                            </div>`
                        }

                        else{

                            let ul = document.querySelector(`.houses${index}`)

                            ul.innerHTML += `<li>${characterList[index].houseName[houses]}</li>`
                            
                        }
                
                        
                        
                    })
                    
                    
                }
                
                
            }

            main.addEventListener('click', e=>{
    
                if(e.target.id == 'button'){
    
                    console.log('Lol');
                }
    
    
            })
        })
        