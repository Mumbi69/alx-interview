#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: node 0-starwars_characters.js <movie_id>')
    process.exit(1)
}

const movieId = process.argv[2]

request(`https: // swapi.dev / api / films /${movieId} /`, (error, response, body)= > {
    if (error) {
        console.error('Error:', error)
        process.exit(1)
    }

    const film=JSON.parse(body)

    film.characters.forEach((characterUrl)=> {
        request(characterUrl, (error, response, body)= > {
            if (error) {
                console.error('Error:', error)
                process.exit(1)
            }

            const character=JSON.parse(body);
            console.log(character.name);
        })
    })
})
