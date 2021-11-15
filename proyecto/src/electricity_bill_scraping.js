const request = require("request");
const cheerio = require('cheerio');

//const url = 'https://www.tarifadeluz.com/mañana.php';
const base_url = "http://www.tarifadeluz.com"


module.exports = {
    scrap: (today=false) => {
        var url = base_url;
        if(!today) url += "/manana.php";

        var p = new Promise((resolve, reject)=>{
            request({
                method: 'GET',
                url: url,
            }, (err, res, body) => {
                if (err) return console.error(err);
                const $ = cheerio.load(body);
                let rows = $("tr").toArray(); // get array of rows, of the page
                
                let price_hour = {}; // initialize array of prices per hour
                for (let i = 3; i < 24+3; i++){
                    // gets the value of the second column of each row starting by the 4th, which happens to 
                    // be the starting of the data's table.
                        // see http://www.tarifadeluz.com and inspect the table to understand it
                    //price_hour.push(rows[i].children[3].children[0].children[0].children[0].data); 
                    price_hour[i-3] = rows[i].children[3].children[0].children[0].children[0].data;
                }
                resolve(price_hour);
            });
        });
        return p;
    }
}

