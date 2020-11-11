// Initialize the page with a default plot
function init() {
    
    d3.json("/api/v1.0/testing_data").then((data) => {

        // Iterate through data
        var id_list = data.map(function(customer) {
            // Collect all customer ID values to populate the drop down
            return customer.id;
        })
        
        // Slice out 50 ID values for site efficiency
        idList20Vals = id_list.slice(0,50);

        // Use D3 to select the location of the drop down values
        let dropdownMenu = d3.select("#customer_ID");

        // Populate the drop down customer ID values
        idList20Vals.forEach(id => {
            dropdownMenu
                .append("option")
                .text(id)
                .property("value", id);;
            });
    
    });
}


// Load init()
init();
