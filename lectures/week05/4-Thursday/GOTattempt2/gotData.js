class Character{
    constructor(name, houseURL, houseName){
        this.name = name
        this.houseURL = houseURL
        this.houseName = houseName

    }
    
    async fetchCharacters(){

        fetchArr = []

        for(let page = 0; page < 43; page++){

            url = fetch(`https://www.anapioficeandfire.com/api/characters?page=${page}&pageSize=50`)
        
            fetchArr.push(url)
        }

        let promise = await Promise.all(fetchArr)

        promise.then(resultsArr=>{

        let newArr = resultsArr.map(char =>{
            return char.json()
        })

            return Promise.all(newArr)
        })

    }

    async fetchHouses(){


    }
}