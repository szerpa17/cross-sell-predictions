// Initialize the page with a default plot
function predict(selectedID) {

    // let selectedID = d3.select("#customer_ID").node().value;
    // console.log(selectedID);
    
    d3.json("/api/v1.0/prediction/"+selectedID).then((data) => {
        let result = Object.values([data.prediction]);
        console.log(result[0])

        // Populate demographic info box
        let box = d3.select("#customer_results");

        // Clear box content
        box.html("");

        // Append customer details items to the box
        box.append("p")
            .text(`${result[0]}`);
            console.log(`${result[0]}`);
        


        // let result = 
        // console.log(data.map(d => d.prediction));
        // // Iterate through data
        // var idList = data.map(function(customer) {
        //     // Collect all customer ID values to populate the drop down
        //     return customer.id;
        // })
        
        // // Slice out 50 ID values for site efficiency
        // idList20Vals = idList.slice(0,50);

        // // Use D3 to select the location of the drop down values
        // let dropdownMenu = d3.select("#customer_ID");

        // // Populate the drop down customer ID values
        // idList20Vals.forEach(id => {
        //     dropdownMenu
        //         .append("option")
        //         .text(id)
        //         .property("value", id);;
        //     });
    
    });
}



// Load init()
init();
