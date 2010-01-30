function shopjet_init() {
	var product_id = shopjet_get_product_id();

    var host = 'http://shopjet.co.il';
    if (document.domain == '127.0.0.1')
        host = 'http://127.0.0.1:8000';

    var store_url = document.domain;
    if (store_url == 'static.shopjet.co.il' || store_url == '127.0.0.1' || store_url == 'shopjet.co.il')
        store_url = 'livesale.co.il';

	var params = 'storeURL=' + encodeURIComponent(store_url) + 
				 '&productId=' + encodeURIComponent(product_id) + 
				 '&callback=?';

	// register handler function in case getJson fails
	$('#shopjet').ajaxError(requestFailed);
	$.getJSON(host + '/products/', params, function(data) {
			requestSucceded(data);
	});
}


function requestSucceded(data) {
	// inject html received from shopjet.co.il
	$('#shopjet').html(data.html);
	// transform all title tags into qTips
	setTips();
	// json request succeded, means we are on 'shopjet' page, track 'view shopjet' event
	trackView('shopjet');
}

function requestFailed() {
	// json request failed, means we are on 'normal' page, track 'view normal' event
	trackView('normal');
}




function trackView(action) {
	  _trackView = action;
}
	
function setTips() {
		$("#shopjet span.glossary").qtip({
			content: {  text: false // use each elements title attribute
						 }, 
			 style: { 
				  title: { 'direction': 'rtl'}, 
				  width: {minimum:100, maximum:250},
				  padding: 5,
				  background: '#A2D959',
				  color: 'black',
				  textAlign: 'right',
				  border: {
					 width: 7,
					 radius: 5,
					 color: '#A2D959'
				  }
			},
			position: {
				corner: {
					target: 'bottomLeft',
					tooltip: 'topRight' } 

					
				}

			});
}

function shopjet_get_product_id() {
    var productid = 0;

    var query = window.location.search;
    if (query.substring(0, 1) == '?') {
        query = query.substring(1);
    }

    // Check all parameters
    var data = query.split('&');
    for (i = 0; (i < data.length); i++) {

        // Check for presence of product id
        var pair = unescape(data[i]).split('=');
        if (pair[0] == 'productid')
            productid = pair[1];

    }

    return productid;
}

$(document).ready(shopjet_init);
