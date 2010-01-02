function shopjet_init() {
	var product_id = shopjet_get_product_id();
	var store_url = 'livesale.co.il'; //document.domain;
	var params = 'storeURL=' + encodeURIComponent(store_url) + 
				 '&productId=' + encodeURIComponent(product_id) + 
				 '&callback=?';
	$.getJSON('http://127.0.0.1:8000/products/', params, function(data) {
		$('#shopjet').html(data.html);
	});
}


function shopjet_get_product_id() {
    /* Dynamically determine the product by inspecting elements in the page */
    return shopjet_product;
}

$(document).ready(shopjet_init);
