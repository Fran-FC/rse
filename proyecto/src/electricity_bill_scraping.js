const request = require("request");
const cheerio = require('cheerio');

const url = "http://www.tarifadeluz.com"

module.exports = {
    scrap: () => {
        var p = new Promise((resolve, reject)=>{
            request({
                method: 'GET',
                url: url,
            }, (err, res, body) => {
                if (err) return console.error(err);
                const $ = cheerio.load(body);
                let rows = $("tr").toArray(); // get array of rows, of the page
                
                let price_hour = new Array(24); // initialize array of prices per hour
                for (let i = 3; i < 24+3; i++){
                    // gets the value of the second column of each row starting by the 4th, which happens to 
                    // be the starting of the data's table.
                        // see http://www.tarifadeluz.com and inspect the table to understand it
                    price_hour[i-3] = parseInt(parseFloat(rows[i].children[3].children[0].children[0].children[0].data)*1000);
                }
                resolve(price_hour);
            });
        });
        return p;
    }
}

