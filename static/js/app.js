// Initialize the page with a default plot
function init() {
    
    d3.json("/api/v1.0/testing_data").then((data) => {

        // Iterate through data
        var idList = data.map(function(customer) {
            // Collect all customer ID values to populate the drop down
            return customer.id;
        })
        
        // Slice out 50 ID values for site efficiency
        idList20Vals = idList.slice(0,50);

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
    console.log(selectedID);
    
    populateInfo(selectedID);
    predict(selectedID);
 }

// Load init()
init();
