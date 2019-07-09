function addItem(tbl) {
// https://stackoverflow.com/questions/49465523/injecting-python-flask-variable-into-html-table-cell-using-javascript

    var table = document.getElementById(tbl);
    console.log(table);
    var tr = document.createElement("tr");
    
    var td1 = document.createElement("td");
    var text1 = document.createTextNode(data.item);
    var td2 = document.createElement("td");
    var text2 = document.createTextNode(data.description)
    var td3 = document.createElement("input");
    var text3 = document.createTextNode("c")
    var td4 = document.createElement("td");
    var text4 = document.createTextNode(data.price)


    td1.appendChild(text1);
    td2.appendChild(text2);
    //td3.appendChild(text3);
    td4.appendChild(text4);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);

    table.appendChild(tr);}

// var addItem = function(items) {
//     // var new_item = '<tr><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><a href="#" id=removeItem">Remove</a></td></tr>'
//     var new_item = 'stuff';
//     //element.insertAdjacentHTML('beforeend', new_item);
//     document.querySelector('.body').insertAdjacentHTML('beforeend', new_item);
// }

/** Commenting out Ajax stuff */
// $(document).ready(function() {

//     var cartBody = $('#cart_body');
//     var customerId = $(this).attr('customer_id')
//     var i = $('#cart_body tr').size() + 1;

//     $('.addItem').on('click', function() {

//         req = $.ajax({
//             url : '/customer/purchase/<customer_id>',
//             type : 'POST',
//             data : {}
//         })
        
//     });

// });





// $(document).on('click', '#addItem', function() {
//     $.ajax({
//     success: function() { $('#cartBody tr').append('<tr><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><a href="#" id=removeItem">Remove</a></td></tr>');
//     i++;
//     return false;
//     }
//     })
// });

// $(document).on('click', '#removeItem', function() {
//     if (i > 2) {
//         $(this).closest('tr').remove();
//         i--;
//     }
//     return false
// });