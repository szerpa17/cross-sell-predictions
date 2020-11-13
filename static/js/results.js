// Initialize the page with a default plot
function predict(selectedID) {

    d3.json("/api/v1.0/prediction/" + selectedID).then((data) => {
        let result = Object.values([data.prediction]);

        // Populate demographic info box
        let box = d3.select("#customer_results");
        let imgBox = d3.select("#rImage")
        
        // Clear box content
        box.html("");
        imgBox.html("");

        // Append customer details items to the box
        box.append("p")
        .text(`${result[0]}`)

        // Conditional to populate result image
        if (result[0] = "Customer is not interested in purchasing car insurance.") {
            imgBox.append("div")
                .html('<img src="https://github.com/szerpa17/cross-sell-predictions/blob/main/images/prediction1.PNG?raw=true" alt="">');

        }

        else {
            imgBox.append("div")
                .html('<img src="https://github.com/szerpa17/cross-sell-predictions/blob/main/images/prediction2.PNG?raw=true" alt="">')

        }
    });
}

