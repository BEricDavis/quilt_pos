
var addItem = function() {
    // var new_item = '<tr><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><input type="text"></td><td><a href="#" id=removeItem">Remove</a></td></tr>'
    var new_item = 'stuff';
    //element.insertAdjacentHTML('beforeend', new_item);
    document.querySelector('.body').insertAdjacentHTML('beforeend', new_item);
}

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