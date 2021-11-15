const scraper = require("./electricity_bill_scraping")
const hours = require("../config/hour_range");
const { next } = require("cheerio/lib/api/traversing");

const first_check = ()=>{
    var price_hour, next_check;
    // first check if it is past 8 pm
    let date = new Date();
    // if it is before 20:15, check prices of today, else, check for tomorrow's
    if (date.getHours() < 20 || (date.getHours() === 20 && date.getMinutes() < 15)) {
        price_hour = await scraper.scrap(today=true);
        next_check = (20*3600+15*60+60) - (date.getHours()*3600+date.getMinutes()*60+date.getSeconds());
    }
    else {
        price_hour = await scraper.scrap();            
        next_check = (24*3600) - (20*3600+15*60+60) - (date.getHours()*3600+date.getMinutes()*60+date.getSeconds());
    }
}

module.exports = {
    start: async ()=>{
    }
}