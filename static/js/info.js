// Create function to build box for customer details        
function populateInfo(selectedID) {

    d3.json("/api/v1.0/" + selectedID).then((data) => {
        let singleCustomer = data;

        // Populate demographic info box
        let box = d3.select("#customer_details");

        // Clear box content
        box.html("");

        // Append customer details items to the box
        for (const [key, value] of Object.entries(singleCustomer[0])) {
            box.append("p")
                .text(`${key}: ${value}`);
            console.log(`${key}: ${value}`);
        };

    });
}
