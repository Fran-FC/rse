const scraper = require("./electricity_bill_scraping")
const hours = require("../config/hour_range")

module.exports = {
    start: ()=>{
        // empezar a calcular 
        
        const price_hour = scraper.scrap();
        console.log(price_hour);
    }
}