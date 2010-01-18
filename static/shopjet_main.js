/* test */
function shopjet_init() {
	var product_id = shopjet_get_product_id();

    var host = 'http://shopjet.co.il';
    if (document.domain == '127.0.0.1')
        host = 'http://127.0.0.1:8000';

    var store_url = document.domain;
    if (store_url == 'shopjet.co.il')
        store_url = 'livesale.co.il';

	var params = 'storeURL=' + encodeURIComponent(store_url) + 
				 '&productId=' + encodeURIComponent(product_id) + 
				 '&callback=?';

	$.getJSON(host + '/products/', params, function(data) {
		$('#shopjet').html(data.html);
	});
}


function shopjet_get_product_id() {
    var productid = 0;

    var query = window.location.search;
    if (query.substring(0, 1) == '?') {
        query = query.substring(1);
    }

    // Check all parameters
    var data = query.split(',');
    for (i = 0; (i < data.length); i++) {

        // Check for presence of product id
        var pair = unescape(data[i]).split('=');
        if (pair[0] == 'productid')
            productid = pair[1];

    }

    return productid;
}

$(document).ready(shopjet_init);
