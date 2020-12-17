// Initialize the page with a default plot
function init() {
    
    d3.json("/api/v1.0/original_customer_data").then((data) => {

        // Iterate through data
        var idList = data.map(function(customer) {
            // Collect all customer ID values to populate the drop down
            return customer.id;
        })
        
        // Loop to populate range
        // Slice out 20 ID values
        var start = 6011;
        var end = 6031;

        var idList20Vals = [];

        while(start < end+1){
            idList20Vals.push(start++);
        }

        // Use D3 to select the location of the drops down values
        let dropdownMenu = d3.select("#customer_ID");

        // Populate the drop down customer ID values
        idList20Vals.forEach(id => {
            dropdownMenu
                .append("option")
                .text(id)
                .property("value", id);;
            });
    
        // Populate initial prediction
        populateInfo(idList20Vals[0])
        predict(idList20Vals[0])
    });
}

function optionChanged() {
    
    let selectedID = d3.select("#customer_ID").node().value;
    
    populateInfo(selectedID);
    predict(selectedID);
 }

// Load init()
init();
