const scraper = require("./electricity_bill_scraping")
const hours = require("../config/hour_range");

const first_check = async ()=>{
    let date = new Date();
    let prices = await scraper.scrap();
    let lowest_price = Math.min(...prices.slice(date.getHours()));
    let lowest_hour = prices.indexOf(lowest_price) + 1;

    return {"hour":lowest_hour, "price": lowest_price/1000}
}

module.exports = {
    start: async()=>{
        let first_res = await first_check();
    }
}
