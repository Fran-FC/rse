const scraper = require("./electricity_bill_scraping")
module.exports = {
    start: ()=>{
        scraper.scrap();
    }
}