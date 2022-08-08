class Character{
    constructor(name, houseURL, houseName){
        this.name = name
        this.houseURL = houseURL
        this.houseName = houseName
        
    }
    
}


const completeCharacterInfo = async (charArr) => {

    let characterObjArr = [];


    for(let i = 0; i < charArr.length; i++){

        let char = new Character((charArr[i].name == "" ? charArr[i].aliases[0] : charArr[i].name), charArr[i].allegiances, [])

        characterObjArr.push(char)
        
    }


    for(let index = 0; index < characterObjArr.length; index++){

        if(characterObjArr[index].houseURL.length == 0){}
        else if (characterObjArr[index].houseURL.length == 1){

            let houses = await fetch(characterObjArr[index].houseURL[0]);
            let results = await houses.json();
            
            characterObjArr[index].houseName.push(results.name)

        }
        else if(characterObjArr[index].houseURL.length > 1){

            for(let i = 0; i < characterObjArr[index].houseURL.length; i++){
                
                let houses = await fetch(characterObjArr[index].houseURL[i]);
                let results = await houses.json();
                
                characterObjArr[index].houseName.push(results.name)
                
            }
        }
    }
    
    let main = document.querySelector('#main')
    let domString =
    `
    <nav class="navbar navbar-1 w-100">
        <div class="container-fluid d-flex justify-content-center">
            <input class="searchBar" type="search" placeholder="Search" aria-label="Search">
            <button class="butt" id="button" type="submit">Search</button>
        </div>
      </nav>
`

    for(let i = 0; i < characterObjArr.length; i++){


        if(characterObjArr[i].houseURL.length == 0){

            domString += `

                        <div class="card1 col-3" id="card" title="${characterObjArr[i].name}">
                            <div class="name" id="card" title="${characterObjArr[i].name}">${characterObjArr[i].name}</div>
                            <div class="allyTag" id="card" title="${characterObjArr[i].name}">Allegiances: None</div>
                        </div>

                        `
        }
        else if(characterObjArr[i].houseURL.length == 1){

            domString += `
                        <div class="card1 col-3" id="card" title="${characterObjArr[i].name}">
                        <div class="name" title="${characterObjArr[i].name}">${characterObjArr[i].name}</div>
                            <div class="allyTag" id="card" title="${characterObjArr[i].name}">Allegiance:</div>
                            <ul id="card" title="${characterObjArr[i].name}">
                                <li id="card" title="${characterObjArr[i].name}">${characterObjArr[i].houseName[0]}</li>
                            </ul>
                        </div>

                         `
        }
        else if(characterObjArr[i].houseURL.length > 1){

            domString += `
                        <div class="card1 col-3" title="${characterObjArr[i].name}" id="card">
                        <div class="name" id="card" title="${characterObjArr[i].name}">${characterObjArr[i].name}</div>
                            <div class="allyTag" title="${characterObjArr[i].name}">Allegiances:</div>
                            <ul id="card" title="${characterObjArr[i].name}">`

            for(let index = 0; index < characterObjArr[i].houseName.length; index++){

                domString += `<li id="card" title="${characterObjArr[i].name}">${characterObjArr[i].houseName[index]}</li>`
            }

            domString += `</ul>
                            </div>`
        }
    }


    main.innerHTML = domString

    
    document.addEventListener('click', e=>{

        let infoBoxName = document.querySelector('.popupName')
        let infoBoxInfo = document.querySelector('.popupInfo')

        if(e.target.id == 'card'){
            

            let targetName = e.target.title

            let characterObj = null

            let allegianceString = ""


            for(let i = 0; i < characterObjArr.length; i++){

                if(targetName == characterObjArr[i].name){

                    characterObj = characterObjArr[i]
                }
            }

            for(let i = 0; i < characterObj.houseName.length; i++){

                console.log(characterObj);

                allegianceString += `${characterObj.houseName[i]}`

                if(i < characterObj.houseName.length -1){

                    allegianceString += `, `
                }
            }

            
            for(let i = 0; i < charArr.length; i++){
                
                if(charArr[i].name == targetName ){
                    
                    infoBoxName.innerHTML += `
                    
                    ${charArr[i].name}
                    `
                    infoBoxInfo.innerHTML += `
                    <div>Allegiances: ${allegianceString} </div>
                    <div>Geneder: ${charArr[i].gender} </div>
                    <div>Culture: ${charArr[i].culture} </div>
                    <div>Born: ${charArr[i].born} </div>
                    <div>Died: ${charArr[i].died} </div>
                    <div>Title: ${charArr[i].titles[0]} </div>
                    `
                }
                else if(charArr[i].aliases[0] == targetName ){
                    
                    infoBoxName.innerHTML += `
                    
                    ${charArr[i].aliases[0]}

                    `

                    infoBoxInfo.innerHTML += `
                    <div>Allegiances: ${allegianceString} </div>
                    <div>Geneder: ${charArr[i].gender} </div>
                    <div>Culture: ${charArr[i].culture} </div>
                    <div>Born: ${charArr[i].born} </div>
                    <div>Died: ${charArr[i].died} </div>
                    <div>Title: ${charArr[i].titles[0]} </div>
                    `
                    
                }
            }

            document.querySelector('.bg-modal').style.display = 'flex';
        }

        if(e.target.id == 'close'){

            document.querySelector('.bg-modal').style.display = 'none';

            infoBoxName.innerHTML = ``
            infoBoxInfo.innerHTML = ``
        }

        if(e.target.id == 'button'){

            let input = document.querySelector('input')

            let targetName = input.value

            let characterObj = null

            let allegianceString = ""
            
            for(let i = 0; i < characterObjArr.length; i++){

                if(input.value == characterObjArr[i].name){
        
        
                    for(let i = 0; i < characterObjArr.length; i++){
        
                        if(targetName == characterObjArr[i].name){
        
                            characterObj = characterObjArr[i]
                        }
                    }
        
                    for(let i = 0; i < characterObj.houseName.length; i++){
        
                        console.log(characterObj);
        
                        allegianceString += `${characterObj.houseName[i]}`
        
                        if(i < characterObj.houseName.length -1){
        
                            allegianceString += `, `
                        }
                    }

                    for(let i = 0; i < charArr.length; i++){
                
                        if(charArr[i].name == targetName ){
                            
                            infoBoxName.innerHTML += `
                            
                            ${charArr[i].name}
                            `
                            infoBoxInfo.innerHTML += `
                            <div>Allegiances: ${allegianceString} </div>
                            <div>Geneder: ${charArr[i].gender} </div>
                            <div>Culture: ${charArr[i].culture} </div>
                            <div>Born: ${charArr[i].born} </div>
                            <div>Died: ${charArr[i].died} </div>
                            <div>Title: ${charArr[i].titles[0]} </div>
                            `
                        }
                        else if(charArr[i].aliases[0] == targetName ){
                            
                            infoBoxName.innerHTML += `
                            
                            ${charArr[i].aliases[0]}
        
                            `
        
                            infoBoxInfo.innerHTML += `
                            <div>Allegiances: ${allegianceString} </div>
                            <div>Geneder: ${charArr[i].gender} </div>
                            <div>Culture: ${charArr[i].culture} </div>
                            <div>Born: ${charArr[i].born} </div>
                            <div>Died: ${charArr[i].died} </div>
                            <div>Title: ${charArr[i].titles[0]} </div>
                            `
                            
                        }
                    }
        
                    document.querySelector('.bg-modal').style.display = 'flex';
                }
                else{}
            }
        }


    })
}



const getChars = async () => {

    let charArr = [];
    let pageIndex = 1;
    let resultsArr = [];

    do{
        let chars = await fetch(`https://www.anapioficeandfire.com/api/characters?page=${pageIndex}&pageSize=50`);
        resultsArr = await chars.json();

        charArr = [...charArr, ...resultsArr]
        pageIndex ++;
    }
    while(resultsArr.length > 0)

    completeCharacterInfo(charArr)

}

getChars()