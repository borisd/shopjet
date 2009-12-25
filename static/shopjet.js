function shopjet_init() {
	var product_id = shopjet_get_product_id();
	var store_url = 'www.sales-shop.com'; //document.domain;
	var sjtc = new Querystring().get('sjtc') || '';
	var params = 'storeURL=' + encodeURIComponent(store_url) + 
				 '&productId=' + encodeURIComponent(product_id) + 
				 '&sjtc=' + encodeURIComponent(sjtc) + '&callback=?';
	$.getJSON('http://localhost/products/', params, function(data) {
		$('#shopjet').html(data.html);
	});
	$(".addthis_toolbox a").live("click", function(e) {
		shopjet_shared(e);
	});
}

function shopjet_shared(e) {
	$(".addthis_toolbox a").die("click");
	var store_url = 'www.sales-shop.com'; //document.domain;
	var tracking_id = document.sjtc;
	$(e.target.parentNode.parentNode).append('<iframe frameborder="0" width="380" height="100" src="http://localhost/generate_tracking/?storeURL=' + store_url + '&tracking_id=' + tracking_id + '">');
}

function shopjet_get_product_id() {
	return 'kick_ass_tv';
}

$(document).ready(shopjet_init);
