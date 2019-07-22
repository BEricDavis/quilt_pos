var getItem = function() {
    console.log('in getItem')
    return {
        item: document.querySelector('.add__item').value,
        description: document.querySelector('.add__description').value,
        price: document.querySelector('.add__price').value,
        quantity: document.querySelector('.add__qty').value,
    }
}

var addItem = function() {
    var html, newHtml, element;
    item = getItem();
    console.log(item)
    // create html with placeholder text
    element = '.cart__items';
    // html = '<div class="item clearfix" id="expense-%id%"><div class="item__description">%description%</div><div class="right clearfix"><div class="item__value">%value%</div><div class="item__percentage">21%</div><div class="item__delete"><button class="item__delete--btn"><i class="ion-ios-close-outline"></i></button></div></div></div>'

    html = '<div class="item clearfix" id="item-%id%">	<div class="item__item">%item%</div><div class="item__description">%description%</div><div class="item__quantity">%quantity%</div><div class="item__price">%price%</div><div class="right clearfix"><div class="item__delete"><button class="item__delete--btn">	<i class="ion-ios-close-outline"></i></button></div></div></div>'

    // replace the placeholder text with data
    newHtml = html.replace('%id%', item.item);
    newHtml = newHtml.replace('%description%', item.description);
    newHtml = newHtml.replace('%value%', item.value);


    // insert html into DOM
    // see lecture 83 
    // https://relxlearning.udemy.com/the-complete-javascript-course/learn/lecture/5869236#content
    document.querySelector(element).insertAdjacentHTML('beforeend', newHtml); 

}



// This addItem method is promising but still falls short
// function addItem(tbl) {
// // https://stackoverflow.com/questions/49465523/injecting-python-flask-variable-into-html-table-cell-using-javascript

//     var table = document.getElementById(tbl);
//     console.log(table);
//     var tr = document.createElement("tr");
    
//     var td1 = document.createElement("input");
//     var text1 = document.createTextNode(data.item);
//     var td2 = document.createElement("input");
//     var text2 = document.createTextNode(data.description)
//     var td3 = document.createElement("input");
//     var text3 = document.createTextNode("c")
//     var td4 = document.createElement("input");
//     var text4 = document.createTextNode(data.price)


//     td1.appendChild(text1);
//     td2.appendChild(text2);
//     //td3.appendChild(text3);
//     td4.appendChild(text4);

//     tr.appendChild(td1);
//     tr.appendChild(td2);
//     tr.appendChild(td3);
//     tr.appendChild(td4);

//     table.appendChild(tr);}

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