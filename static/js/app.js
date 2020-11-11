// Initialize the page with a default plot
function init() {

    d3.json("/api/v1.0/testing_data").then((data) => {

        var id_list = data.map(function(customer) {
            return customer.id
        })
        
        console.log(id_list)
        // })
        // let id_values = data.map(callback(currentValue[, index[, array]]) {
        //     console.log(currentValue);
        // //     // return element for newArray, after executing something
        //   });


        // let dropdownMenu = d3.select("select");
        // data.id.forEach(ids => {
        //     dropdownMenu.append("option").text(ids);
        //     });
    
    });
}


// Load init()
init();
