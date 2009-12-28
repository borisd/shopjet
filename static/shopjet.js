function shopjet_init() {
	var product_id = shopjet_get_product_id();
	var store_url = 'www.sales-shop.com'; //document.domain;
	var params = 'storeURL=' + encodeURIComponent(store_url) + 
				 '&productId=' + encodeURIComponent(product_id) + 
				 '&callback=?';
	$.getJSON('http://127.0.0.1:8000/products/', params, function(data) {
		$('#shopjet').html(data.html);
	});
}


function shopjet_get_product_id() {
	return 'kick_ass_tv';
}

$(document).ready(shopjet_init);
