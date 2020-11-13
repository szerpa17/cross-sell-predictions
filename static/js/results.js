// Initialize the page with a default plot
function predict(selectedID) {

    // let selectedID = d3.select("#customer_ID").node().value;
    // console.log(selectedID);

    d3.json("/api/v1.0/prediction/" + selectedID).then((data) => {
        let result = Object.values([data.prediction]);
        console.log(result[0])

        // Populate demographic info box
        let box = d3.selectAll("#customer_results");

        // Clear box content
        box.html("");

        // Conditional to populate image
        if (result = "Customer not interested") {
            // Append customer details items to the box
            box.append("p")
                .text(`${result[0]}`)
            // console.log(;`${result[0]}`);
            box.append("div")
                .html('<img src="https://github.com/szerpa17/cross-sell-predictions/blob/main/images/prediction1.PNG?raw=true" alt="">')
                // .attr('class', "border-radius: 20px")
                .style("border-radius", "8px");
        }
        else {
            box.append("p")
                .text(`${result[0]}`)
            // console.log(;`${result[0]}`);
            box.append("div")
                .html('<img src="https://github.com/szerpa17/cross-sell-predictions/blob/main/images/prediction2.PNG?raw=true" alt="">')
                // .attr('class', "border-radius: 20px")
                .style("border-radius", "8px");
        }


    });
}



// Load init()
init();
