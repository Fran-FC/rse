const request = require("request");
const cheerio = require('cheerio');

const url = 'https://tarifaluzhora.es';

module.exports = {
    scrap: () => {
        request({
            method: 'GET',
            url: url,
        }, (err, res, body) => {
            if (err) return console.error(err);
            let $ = cheerio.load(body);
            let precioHora = $(".sub_text.col-sm-12");
            precioHora = precioHora.text().replace(/\s/g,'').replace('€/kWh', '');
            console.log(precioHora);
            
            //handlePrice(precioHoy);
        });
    }
}

