// Create function to build box for customer details        
// Function to capitalize text for labels (ignoring words under the length of 4)
function capitalizeEachWord(str) {
    // Conditional to check if the string has any wite spaces
    if (/\s/.test(str)){
        // Return each word in the string
        return str.replace(/\w\S*/g, function(txt) {
            // If The word is more than 3 characters long, capitalize the first letter
            if (txt.length >3) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
            // Else do not capitalize
            else {
                return txt;
            }
            });
    }
    // If the string only has a single word, regardless of the length of the word - capitalize the first letter.
    else {
        return str.charAt(0).toUpperCase()+ str.substr(1).toLowerCase();
    }
}

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
                .text(`${capitalizeEachWord(key)}: ${value}`);
            console.log(`${capitalizeEachWord(key)}: ${value}`);
        };

    });
}
